# Please Edit this Doc!

SLINGSHOT Code Challenge #7

## Problem statement

We all know how to edit documents on Word. However, to date, there's no good open source implementation of a .docx editor in npm/javascript. Most solutions out there are paid -- the goal is to make something better and free for the world to use. 

## Solution

I propose a web app that can be used to edit the contents of a .docx file in markdown, and be able to translate/export the markdown back into .docx or HTML. This will not only allow people to quickly transfer between document types, but allow people to change the document as well.

Here's a [YouTube demo](https://youtu.be/FEODL2FJz0E) of the code.

Here's the deployed [app](https://kevinh45-edit-doc-app-dtisl1.streamlitapp.com/).

I am aware of some features of .docx being incorrectly converted to markdown (equations and tables), please submit a PR if you want to solve this.

## Dependencies and resources

- [Mammoth](https://pypi.org/project/mammoth/)
- [Python-Markdown](https://pypi.org/project/Markdown/) and [Markdownify](https://pypi.org/project/markdownify/)
- [Streamlit](https://streamlit.io/)
- For full list of dependencies, view `requirements.txt`
- Credit to cytronicoder for the README format and the .gitignore.



