from collections.abc import Sequence

from ...types import BBoxKind
from ..bbox_img import BBoxImg
from .editor import RelBBoxEditor


class RelBBox(RelBBoxEditor, BBoxImg):
    def __init__(
        self,
        coords: Sequence,
        kind: BBoxKind | str = "x1y1x2y2",
        text: str = "",
        **kwargs,
    ):
        super().__init__(coords, kind)
        self.text = text
        self.__dict__.update(kwargs)

    def crop_from(self, img):
        h, w, *c = img.shape
        x1 = round(self.x1 * w)
        x2 = round(self.x2 * w)
        y1 = round(self.y1 * h)
        y2 = round(self.y2 * h)

        return img[y1:y2, x1:x2]

    def is_valid(self):
        comment = "Use only float coords in range [0, 1]"
        assert (
            (0.0 <= self.x1 <= 1.0)
            and (0.0 <= self.y1 <= 1.0)
            and (0.0 <= self.x2 <= 1.0)
            and (0.0 <= self.y2 <= 1.0)
        ), comment
        super().is_valid()

    def as_abs(self, img_w: int, img_h: int):
        from ..abs.abs_bbox import AbsBBox

        x1, y1, x2, y2 = self.get_pascal_voc()
        x1 = round(x1 * img_w)
        y1 = round(y1 * img_h)
        x2 = round(x2 * img_w)
        y2 = round(y2 * img_h)
        return AbsBBox((x1, y1, x2, y2), text=self.text)

    def __repr__(self):
        bbox = (
            f"RelBBox(x1={round(self.x1, 3)}, y1={round(self.y1, 3)}, "
            f"x2={round(self.x2, 3)}, y2={round(self.y2, 3)})"
        )
        if text := self.text:
            text = f" - {self.text}"
        return f"<{bbox}{text}>"
