# -*- coding: utf-8 -*-
import csv
import logging
import shutil
import tempfile
from collections import defaultdict
from itertools import chain, repeat
from pathlib import Path
from typing import Optional
from uuid import UUID

from arkindex_cli.auth import Profiles
from arkindex_cli.commands.elements.utils import retrieve_children

logger = logging.getLogger(__name__)

CSV_HEADER_DEFAULT = [
    "id",
    "name",
    "type",
    "image_id",
    "image_url",
    "polygon",
    "worker_version_id",
    "created",
]
CSV_HEADER_CLASSES = CSV_HEADER_DEFAULT + [
    "class_name",
    "class_id",
    "classification_confidence",
]


class ElementsList:
    """
    List elements from a given corpus or parent element.
    """

    def __init__(
        self,
        api_client,
        corpus: Optional[UUID] = None,
        parent: Optional[UUID] = None,
        type: Optional[str] = None,
        recursive: Optional[bool] = False,
        with_classes: Optional[bool] = False,
        with_metadata: Optional[bool] = False,
        output_path: Optional[Path] = None,
    ):
        self.client = api_client
        self.corpus = corpus
        self.parent = parent
        self.type = type
        self.recursive = recursive
        self.with_classes = with_classes
        self.with_metadata = with_metadata

        if output_path is None:
            output_path = Path.cwd() / "elements.csv"
        self.output_path = output_path

        # Since one metadata can be set multiple times, with different values, on one element,
        # we need to know the maximum count for each metadata across all listed elements in
        # order to be able to add as many columns for each metadata as its max count
        self.metadata = {}
        self.metadata_names_max_counts = {}

    def serialize_child(self, child):
        """
        Takes an element as input, and outputs one or more dictionaries to be used
        by writerow, depending on the with_classes parameter and whether an element
        has classes or not (if an element has n classes, yields n dictionaries)
        """

        classes = child.get("classes")
        metadata = child.get("metadata")
        base_dict = {
            "id": child["id"],
            "name": child["name"],
            "type": child["type"],
            "image_id": None,
            "image_url": None,
            "polygon": None,
            "worker_version_id": child["worker_version_id"],
            "created": child["created"],
        }
        if child.get("zone"):
            base_dict["image_id"] = child["zone"]["image"]["id"]
            base_dict["image_url"] = child["zone"]["image"]["url"]
            base_dict["polygon"] = child["zone"]["polygon"]

        if self.with_metadata:
            self.metadata[child["id"]] = defaultdict(list)
            for item in metadata:
                self.metadata[child["id"]][item["name"]].append(item["value"])
            # Get the values count for each metadata; if the metadata already has a values count
            # in self.metadata_names_max_counts and the new count is bigger, update it; else save
            # that count.
            for metadata_name, values in self.metadata[child["id"]].items():
                self.metadata_names_max_counts[metadata_name] = max(
                    len(values), self.metadata_names_max_counts.get(metadata_name, 0)
                )

        if self.with_classes:
            if classes:
                for one_class in classes:
                    yield {
                        **base_dict,
                        **{
                            "class_name": one_class["ml_class"]["name"],
                            "class_id": one_class["id"],
                            "classification_confidence": one_class["confidence"],
                        },
                    }
            else:
                yield {
                    **base_dict,
                    **{
                        "class_name": None,
                        "class_id": None,
                        "classification_confidence": None,
                    },
                }
        else:
            yield base_dict

    def metadata_columns(self):
        columns = list(
            chain.from_iterable(
                repeat(f"metadata_{name}", count)
                for name, count in self.metadata_names_max_counts.items()
            )
        )
        return columns

    def write_to_csv(self, elements, tmp_file):
        csv_header = CSV_HEADER_CLASSES if self.with_classes else CSV_HEADER_DEFAULT

        with open(tmp_file.name, "w", encoding="UTF8", newline="") as output:
            writer = csv.DictWriter(output, fieldnames=csv_header)
            writer.writeheader()

            for item in elements:
                for item in self.serialize_child(item):
                    writer.writerow(item)

    def run(self):
        children = retrieve_children(
            self.client,
            corpus=self.corpus,
            parent=self.parent,
            type=self.type,
            recursive=self.recursive,
            with_classes=self.with_classes,
            with_metadata=self.with_metadata,
        )

        with tempfile.NamedTemporaryFile() as tmp_file:
            self.write_to_csv(children, tmp_file)

            if self.with_metadata:
                with open(tmp_file.name, "r") as input:
                    reader = csv.reader(input)
                    csv_header = next(reader)
                    with open(
                        self.output_path, "w", encoding="UTF8", newline=""
                    ) as output:
                        metadata_columns = self.metadata_columns()
                        csv_header = csv_header + metadata_columns
                        writer = csv.writer(output)
                        writer.writerow(csv_header)
                        for row in reader:
                            # The element ID is the first item in each row
                            element_metadata = self.metadata[row[0]]
                            for (
                                class_name,
                                max_count,
                            ) in self.metadata_names_max_counts.items():
                                if class_name not in element_metadata:
                                    row.extend(repeat(None, max_count))
                                else:
                                    # Fill the columns with the metadata values and blanks if necessary
                                    i = 0
                                    while i <= max_count - 1:
                                        row.append(
                                            element_metadata[class_name][i]
                                            if i
                                            <= len(element_metadata[class_name]) - 1
                                            else None
                                        )
                                        i += 1
                            writer.writerow(row)
            else:
                shutil.copy2(tmp_file.name, self.output_path)
            logger.info(f"Listed elements successfully written to {self.output_path}.")


def add_list_parser(subcommands):
    list_parser = subcommands.add_parser(
        "list",
        description="List all elements in a corpus or under a specified parent and output results in a CSV file.",
        help="",
    )
    root = list_parser.add_mutually_exclusive_group(required=True)
    root.add_argument(
        "--corpus",
        help="UUID of an existing corpus.",
        type=UUID,
    )
    root.add_argument(
        "--parent",
        help="UUID of an existing parent element.",
        type=UUID,
    )
    list_parser.add_argument(
        "--type",
        help="Limit the listing using this slug of an element type.",
        type=str,
    )
    list_parser.add_argument(
        "--recursive",
        help="List elements recursively.",
        action="store_true",
    )
    list_parser.add_argument(
        "--with-classes",
        help="List elements with their classifications.",
        action="store_true",
    )
    list_parser.add_argument(
        "--with-metadata",
        help="List elements with their metadata.",
        action="store_true",
    )
    list_parser.add_argument(
        "--output",
        default=Path.cwd() / "elements.csv",
        type=Path,
        help="Path to a CSV file where results will be outputted. Defaults to '<current_directory>/elements.csv'.",
        dest="output_path",
    )
    list_parser.set_defaults(func=run)


def run(
    profile_slug: Optional[str] = None,
    gitlab_secure_file: Optional[Path] = None,
    **kwargs,
):
    profiles = Profiles(gitlab_secure_file)
    api_client = profiles.get_api_client_or_exit(profile_slug)
    ElementsList(api_client, **kwargs).run()
