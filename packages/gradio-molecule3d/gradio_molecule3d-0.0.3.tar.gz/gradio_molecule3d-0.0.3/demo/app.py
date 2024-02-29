
import gradio as gr
from gradio_molecule3d import Molecule3D

import os

example = Molecule3D().example_inputs()


reps =    [
    {
      "model": 0,
      "chain": "",
      "resname": "",
      "style": "cartoon",
      "color": "whiteCarbon",
      "residue_range": "",
      "around": 0,
      "byres": False,
      "visible": False,
    },
  ]

def predict(x):
    print("predict function", x)
    return x

#doesn't work
#demo = gr.Interface(
#     predict,
#     Molecule3D(label="Molecule3D", reps=reps),  # interactive version of your component
#     Molecule3D(),  # static version of your component
#     examples=[[example]],  # uncomment this line to view the "example version" of your component
# )

#works
with gr.Blocks() as demo:
    inp = Molecule3D("demo/1pga.pdb",label="Molecule3D", reps=reps)
    inp = Molecule3D("demo/1pga.pdb",label="Molecule3D", reps=reps, showviewer=False)
    out = Molecule3D(label="Molecule3D", reps=reps)
    btn = gr.Button("Predict")
    btn.click(predict, inputs=inp, outputs=out)

demo.launch()
# blocks.launch()
