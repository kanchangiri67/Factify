from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes

class FactifyTheme(Base):
    def __init__(self):
        super().__init__(
            primary_hue=colors.orange,
            secondary_hue=colors.blue,
            neutral_hue=colors.gray,
            font=[
                fonts.GoogleFont("Quicksand"),
                "ui-sans-serif",
                "sans-serif",
            ],
            text_size=sizes.text_md,
        )
        super().set(
            body_background_fill="white",
            button_primary_background_fill="*primary_400",
            button_primary_text_color="white",
            block_title_text_weight="bold",
            block_shadow="*shadow_drop_lg",
        )

custom_theme = FactifyTheme()
