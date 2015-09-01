from openedx.core.lib.block_cache.transformer import BlockStructureTransformer


class StudentViewTransformer(BlockStructureTransformer):
    """
    ...
    """
    VERSION = 1
    STUDENT_VIEW_DATA = 'student_view_data'
    STUDENT_VIEW_MULTI_DEVICE = 'student_view_multi_device'

    @classmethod
    def collect(cls, block_structure):
        """
        Collect student_view_multi_device and student_view_data values for each block
        """
        for block_key in block_structure.topological_traversal():
            block = block_structure.get_xblock(block_key)
            block_structure.set_transformer_block_data(
                block_key,
                cls,
                cls.STUDENT_VIEW_MULTI_DEVICE,
                block.has_support(getattr(block, 'student_view', None), 'multi_device'),
            )
            if getattr(block, 'student_view_data', None):
                block_structure.set_transformer_block_data(
                    block_key,
                    cls,
                    cls.STUDENT_VIEW_DATA,
                    block.student_view_data(),
                )

    def transform(self, user_info, block_structure):
        """
        Mutates block_structure based on the given user_info.
        """
        pass
