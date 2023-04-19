# Psytoolkit Questionnaire Formatter <img src="images/brain.png" align="right" height="138" alt="" />

<!-- badges: start -->

![GitHub release (latest by date)](https://img.shields.io/github/v/release/jakub-jedrusiak/Psytoolkit-Questionnaire-Formatter)
![GitHub](https://img.shields.io/github/license/jakub-jedrusiak/Psytoolkit-Questionnaire-Formatter)
<a href="https://twitter.com/intent/follow?screen_name=jakub_jedrusiak">
![Twitter Follow](https://img.shields.io/twitter/follow/jakub_jedrusiak?style=social)
</a>

<!-- badges: end -->

A simple python tool for fast conversion of questionnaires into [PsyToolkit](https://www.psytoolkit.org/) format.

![gif example](images/example.gif)

## Installing

### Source code

Best way to run this script is to use python source file. Make sure to install [python](https://www.python.org/) beforehand and chcek *Add python to PATH* while installing. `customtkinter` and `pillow` modules is currently needed, so you need to install it by opening the terminal window and typing:

```bash
pip install customtkinter
```

```bash
pip install pillow
```

### Windows executable

Use [releases](https://github.com/jakub-jedrusiak/Psytoolkit-Questionnaire-Formatter/releases) to download the current .exe file. Known problems include a need to click on something multiple times before it starts to work.

## Scoring

This tool allows for setting scores for the questionnaire's items as well as **reversing scores for selected items**. To add scores to your scale, use appropriate buttons. You can use settings to change scoring convention (incremental, decremental or fixed for manually adding a the scoring without having to write `{score=X}` each time). To reverse the scale for an item, add an asterisk `*` at the end of the item. Reversing uses the input order and ignores items that are not scored.

## Multiple questions per page

To make some of the questions appear on the same page, write enclose them in `----` (four dashes) or with `page: begin` and `page: end` tags. These are special lines and will not be treated as questions to format.

## Example

```text
page: begin
I feel that I am a person of worth, at least on an equal plane with others.
I feel that I have a number of good qualities.
All in all, I am inclined to feel that I am a failure.*
I am able to do things as well as most other people.
I feel I do not have much to be proud of.*
I take a positive attitude toward myself.
On the whole, I am satisfied with myself.
I wish I could have more respect for myself.
I certainly feel useless at times.*
At times I think I am no good at all.*
page: end
```

Above text can  be used to create a Rosenberg Self-Esteem Scale (Rosenberg, 1965) questionnaire with 10 items. The items marked with an asterisk will have reversed scoring (if it's used). The `page: begin` and `page: end` tags will cause all the items to appear on the same page.

## To-do

- [X] Options like random, requied etc.
- [X] Scoring
- [X] radio
- [X] drop
- [X] check
- [ ] scale
- [ ] range
- [ ] textline
- [ ] textbox
- [X] rank
- [X] info
- [ ] images
- [ ] sounds
- [ ] videos
- [ ] time options
- [X] multiple questions per page

## Note

This is a community tool. I'm not a PsyToolkit developer nor author. That would be prof. Gijsbert Stoet.

## Bibliography

<div class="csl-bib-body" style="line-height: 2; margin-left: 2em; text-indent:-2em;">
  <div class="csl-entry">Rosenberg, M. (1965). <i>Society and the adolescent self-image</i>. Princeton: Princeton University Press.</div>
  <div class="csl-entry">Stoet, G. (2010). PsyToolkit: A software package for programming psychological experiments using Linux. <i>Behavior Research Methods</i>, <i>42</i>(4), 1096–1104. <a href=https://doi.org/10.3758/BRM.42.4.1096>https://doi.org/10.3758/BRM.42.4.1096</a></div>
  <div class="csl-entry">Stoet, G. (2017). Psytoolkit: A novel web-based method for running online questionnaires and reaction-time experiments. <i>Teaching of Psychology</i>, <i>44</i>(1), 24–31. <a href=https://doi.org/10.1177/0098628316677643>https://doi.org/10.1177/0098628316677643</a></div>
</div>
