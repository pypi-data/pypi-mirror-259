"""gr.Model4DGS() component."""

from __future__ import annotations

from pathlib import Path
from typing import Callable, List

from gradio_client.documentation import document, set_documentation_group

from gradio.components.base import Component
from gradio.data_classes import FileData, GradioModel
from gradio.events import Events

set_documentation_group("component")

class Model4DGSData(GradioModel):
    files: List[FileData]

@document()
class Model4DGS(Component):
    """
    Component allows users to upload or view 4D Gaussian Splatting files (.splat).
    Preprocessing: This component passes the uploaded file as a {str}filepath.
    Postprocessing: expects function to return a {str} or {pathlib.Path} filepath of type (.splat)
    """

    EVENTS = [Events.change, Events.upload, Events.edit, Events.clear]

    data_model = Model4DGSData

    def __init__(
        self,
        value: str | Callable | None = None,
        *,
        height: int | None = None,
        label: str | None = None,
        show_label: bool | None = None,
    ):
        """
        Parameters:
            value: path to (.splat) file to show in model4DGS viewer. If callable, the function will be called whenever the app loads to set the initial value of the component.
            height: height of the model4DGS component, in pixels.
        """
        self.height = height
        super().__init__(
            label=label,
            show_label=show_label,
            value=value,
        )

    def preprocess(self, payload: List[str] | None) -> List[str] | None:
        return payload

    def postprocess(self, value: List[str] | str | None) -> List[FileData] | None:
        if value is None:
            return value
        if isinstance(value, list):
            return [FileData(path=file) for file in value]
        return FileData(path=value)

    # example display name
    def as_example(self, input_data: List[str] | str | None) -> str:
        return Path(input_data).name if input_data else ""

    def example_inputs(self):
        return [
            "assets/tiger_4d_model_0.ply",
            "assets/tiger_4d_model_1.ply",
            "assets/tiger_4d_model_2.ply",
            "assets/tiger_4d_model_3.ply",
            "assets/tiger_4d_model_4.ply",
            "assets/tiger_4d_model_5.ply",
            "assets/tiger_4d_model_6.ply",
            "assets/tiger_4d_model_7.ply",
            "assets/tiger_4d_model_8.ply",
            "assets/tiger_4d_model_9.ply",
            "assets/tiger_4d_model_10.ply",
            "assets/tiger_4d_model_11.ply",
            "assets/tiger_4d_model_12.ply",
            "assets/tiger_4d_model_13.ply"
            ];