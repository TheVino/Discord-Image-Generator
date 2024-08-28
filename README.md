




# Discord-Image-Generator🖼️

Hi! This program can generate images from a prompt and send on a discord channel (*or to an user directly*) using 2 different AI model generators.
<img src="https://avatars.githubusercontent.com/u/1965106?s=200&v=4" alt="drawing" width="20"/>
 

# What libs do I need? 
<img src="https://imgur.com/oMCL4sP.png" alt="drawing" width="400"/>


## Before you start coding
##### You will need an API key (*for model usage access*) and Discord Token (*for discord bot auth*)
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRv_QSMmUfokI2IrDInISWyDxmlLJC1njGsj_KVCcm1p_zi5y_j)

Please check these 3 links and generate your keys:
- Stability AI: https://platform.stability.ai/account/keys 
- Discord: https://discord.com/developers/applications
- Hugging Face: https://huggingface.co/settings/tokens

## Main code has these functions

- Generate image locally free but less porwerfull tool
- Generate image with minimum cost but more porwerfull tool
- Generate image locally free but more porwerfull tool

*All of these will send to discord channel or user who sent the prompt*

## Testing the program! 👨‍💻
![](https://i.imgur.com/2bkRMyk.png)
Will read the prompt and generate the image using Stable Diffusion 1.5 and CUDA

![](https://i.imgur.com/W7N4tXs.png)
Will read the prompt and generate the image using Stable Diffusion 3 on cloud

<img src="https://i.imgur.com/Sm7Y4QT.png" alt="drawing" width="400"/>

Will print on terminal when the bot is connected to Discord

![](https://i.imgur.com/7ohTgFi.png)
Will listen to events when called on Discord and execute accordingly

# How the bot looks like and responds
My face 😊 (some stylish to polish the bot's visual - *all configurable on discord devs webpage*)
![](https://i.imgur.com/7Vor6mi.png)

``When generating with >gen``

<img src="https://i.imgur.com/QBfnMeZ.png" alt="drawing" width="500"/>
<img src="https://i.imgur.com/ssU3Yoa.png" alt="drawing" width="500"/>


``When generating with >gen2``

Unfortunatelly I used all my resources with stable difusion 3 model on cloud generation (and local models are so heavy and GPU demanding that I was not prepared to wait minutes to generate each image using this tool 😵‍💫)
<img src="https://i.imgur.com/tX4onXE.png" alt="drawing" width="500"/>

> But for science purposes, I have 1 example generated locally with Stable Diffusion 3:
![](https://i.imgur.com/GzXoEGa.png)


*This example took 75minutes on a 3080TI @100% usage with 170 Watts (Pytorch and tensor models were not even optmized for my system)*

### Hidden features:

- It blocks **NSFW** content if you try to seach
![](https://i.imgur.com/2fOjBBC.png)

### Future Features:
- Use Stable Diffusion 3 Locally and optimized (*without [ComfyUI](https://github.com/comfyanonymous/ComfyUI) cause I hate their complexness and UI decision*)
- Better integration on Discord with more options and tools
- User Manual for ">help" prompt
