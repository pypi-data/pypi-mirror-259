import jupytext
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pathlib
import os
import sys
import inspect
import pypandoc
import docx2pdf  # Requires MS Word


class Publication:
    def __init__(
        self, title, author, source_filename=None, source_kind="script"
    ):
        if self.is_notebook():
            self.nowrite = True  # Don't want to write if executed from within an ipynb (infinite loop)
        else:
            self.nowrite = False
            self.title = title
            self.author = author
            if not source_filename:  # Then use the calling file
                source_filename = pathlib.Path(
                    inspect.getframeinfo(sys._getframe(1)).filename
                )
            self.subtitle = (
                "Source Filename: "
                + f"{source_filename.parent.stem}/{source_filename.name}"
            )
            self.source_kind = source_kind
            self.source_filename = source_filename
            self.basename = self.basenamer(source_filename)
            self.jupytext = jupytext.read(source_filename)
            if source_kind == "script":
                self.write(to="ipynb-tmp", tmp=True, clean=False)
                self.pypandoc = pypandoc.convert_file(
                    f".tmp_{self.basename}.ipynb", "rst"
                )
                self.cleanup()
            elif source_kind == "ipynb":
                self.pypandoc = pypandoc.convert_file(
                    source_filename, "rst"
                )
            else:
                raise ValueError(f"Unknown source_kind={source_kind}")

    def basenamer(self, filename):
        return pathlib.Path(filename).stem

    def run(self):
        self.write(to="ipynb-tmp", tmp=True, clean=False)
        with open(f".tmp_{self.basename}.ipynb") as f:
            nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
        ep.preprocess(nb, {"metadata": {"path": "."}})
        with open(
            f".tmp_{self.basename}_executed.ipynb",
            "w",
            encoding="utf-8",
        ) as f:
            nbformat.write(nb, f)

    def filter_absolute_path(self):
        return pathlib.Path(__file__).parent / "filter.lua"

    def reference_doc_absolute_path(self):
        return pathlib.Path(__file__).parent / "pandoc_reference.docx"

    def write(self, to: str, pdflatex=False, tmp=False, clean=True):
        if self.nowrite:
            return None
        else:
            if tmp:
                tmp_str = ".tmp_"
            else:
                tmp_str = ""
            if to == "ipynb":
                jupytext.write(
                    self.jupytext, f"{tmp_str}{self.basename}_pub.ipynb"
                )
            elif to == "ipynb-tmp":
                jupytext.write(
                    self.jupytext, f"{tmp_str}{self.basename}.ipynb"
                )
            elif to == "md" or to == "pdf" or to == "docx":
                self.run()
                tmp_nb_executed = f".tmp_{self.basename}_executed.ipynb"
                if to == "md":
                    self.write(to="ipynb-tmp", tmp=True, clean=False)
                    output = pypandoc.convert_file(
                        tmp_nb_executed,
                        "md",
                        outputfile=f"{tmp_str}{self.basename}_pub.md",
                    )
                    assert output == ""
                elif to == "pdf":
                    if pdflatex:
                        self.write(
                            to="ipynb-tmp", tmp=True, clean=False
                        )
                        output = pypandoc.convert_file(
                            tmp_nb_executed,
                            "pdf",
                            outputfile=f"{tmp_str}{self.basename}_pub.pdf",
                        )
                        assert output == ""
                    else:
                        self.write(to="docx", tmp=True, clean=False)
                        docx2pdf.convert(
                            f".tmp_{self.basename}_pub.docx",
                            f"{self.basename}_pub.pdf",
                        )
                elif to == "docx":
                    self.write(to="ipynb-tmp", tmp=True, clean=False)
                    filters = [str(self.filter_absolute_path())]
                    extra_args = [
                        "--reference-doc",
                        str(self.reference_doc_absolute_path()),
                        f"--metadata=title:{self.title}",
                        f"--metadata=subtitle:{self.subtitle}",
                        f"--metadata=author:{self.author}",
                    ]
                    output = pypandoc.convert_file(
                        tmp_nb_executed,
                        "docx",
                        outputfile=f"{tmp_str}{self.basename}_pub.docx",
                        extra_args=extra_args,
                        filters=filters,
                    )
                    assert output == ""
            else:
                raise ValueError(f"Unkown target (to) format: {to}")
            if clean:
                self.cleanup()

    def cleanup(self):
        for filename in pathlib.Path(".").glob(".tmp*"):
            filename.unlink()

    def is_notebook(self) -> bool:
        try:
            shell = get_ipython().__class__.__name__
            if shell == "ZMQInteractiveShell":
                return True  # Jupyter notebook or qtconsole
            elif shell == "TerminalInteractiveShell":
                return False  # Terminal running IPython
            else:
                return False  # Other type (?)
        except NameError:
            return False  # Probably standard Python interpreter
