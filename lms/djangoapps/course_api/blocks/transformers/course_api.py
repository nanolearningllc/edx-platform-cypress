from openedx.core.lib.block_cache.transformer import BlockStructureTransformer
from course_api.blocks.transformers.block_counts import BlockCountsTransformer
from course_api.blocks.transformers.student_view import StudentViewTransformer


class CourseAPITransformer(BlockStructureTransformer):
    """
    ...
    """
    VERSION = 1
    STUDENT_VIEW_DATA = 'student_view_data'
    STUDENT_VIEW_MULTI_DEVICE = 'student_view_multi_device'

    def __init__(self, block_counts):
        self.block_counts = block_counts

    @classmethod
    def collect(cls, block_structure):
        """
        Collects any information that's necessary to execute this transformer's
        transform method.
        """
        # collect basic xblock fields
        block_structure.request_xblock_fields('graded', 'format', 'display_name', 'type')

        # collect data from containing transformers
        StudentViewTransformer.collect(block_structure)
        BlockCountsTransformer.collect(block_structure)

        # TODO support olx_data by calling export_to_xml(?)

    def transform(self, user_info, block_structure):
        """
        Mutates block_structure based on the given user_info.
        """
        StudentViewTransformer().transform(user_info, block_structure)
        BlockCountsTransformer(self.block_counts).transform(user_info, block_structure)
