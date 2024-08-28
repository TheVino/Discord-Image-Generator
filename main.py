import os, uuid, torch, discord, requests
from diffusers import StableDiffusionPipeline   # For v1.5
from diffusers import StableDiffusion3Pipeline  # For v3.0 

# Just needed if the system send warning messages
# os.environ['TF_CPP_MIN_LOH_LEVEL'] = '3'

model_id = "runwayml/stable-diffusion-v1-5"     # defines the model. model 3 can be an option and has better responses
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")  # defines the FPU Usage for this generator

# Loading the keys
API = open('API.pfx', 'r').read()
TOKEN = open('token.txt', 'r').read()

# Permissions
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

def gen(prompt): # stable diffusion 1.5. Free to use, but requires local processing 
    filename = f"{prompt}.png"
    image = pipe(prompt).images[0]
    image.save(filename)
    return filename

def gen2(prompt, API): # stable Diffusion 3. Requires API key and paid usage
    response = requests.post(
            f"https://api.stability.ai/v2beta/stable-image/generate/ultra",
            headers={
                "authorization": API,
                "accept": "image/*"
            },
            files={"none": ''},
            data={
                "prompt": prompt,
                "output_format": "png",
            },
        )
    
    filename = f"{prompt}.png"
        
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        status = True
    else:
        error_response = response.json()
        print(error_response["name"])
        status = error_response["name"]
        # raise Exception(str(response.json()))
    return filename, status

@client.event
async def on_connect():
    print('Bot connected')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('>gen '):
        await message.channel.send(f'Generating image for prompt "{message.content[5:]}"...')
        filename = gen(message.content[5:])
        with open(filename, 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
        os.remove(filename)
        
    if message.content.startswith('>gen2 '):
        await message.channel.send(f'Generating image for prompt "{message.content[6:]}"...')

        filename, status = gen2(message.content[6:], API)
        if status == True:
            with open(filename, 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file=picture)
        else:
            await message.channel.send(f'Error generating image :( \nDetails: "{status}"')

    

client.run(TOKEN)