import sys
import logging
from linkml.generators.docgen import DocGenerator

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error(
            "Usage: `poetry run python src/scripts/term_list_generator.py <output-file.md>`"
        )
        sys.exit(1)

    output_file = sys.argv[1]

    docgen = DocGenerator("src/mixs_6_2_for_merge/schema/mixs_6_2_for_merge.yaml", directory="docs")
    terms = list(docgen.all_slot_objects())

    try:
        with open(output_file, "w") as md_file:
            md_file.write("# List of all terms in MIXS schema\n\n")

            md_file.write("| Name | Description |\n")
            md_file.write("| --- | --- |\n")

            for t in terms:
                description = t.description
                link = docgen.link(t.name)
                md_file.write(f"| {link} | {description} |\n")

        logger.info(f"Term list table has been written to '{output_file}'.")
    except Exception as e:
        logger.error(f"Error writing to '{output_file}': {str(e)}")
