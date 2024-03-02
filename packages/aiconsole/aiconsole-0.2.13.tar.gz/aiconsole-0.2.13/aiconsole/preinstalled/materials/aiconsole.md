## Core messanging

Claim: Open Source Desktop Alternative to OpenAI GPTs

### Run Code Locally

Run it locally; the console can perform all the tasks that your machine is capable of executing.

### Improves with Use

Describe in plain text how to perform a given task once, and thereafter AIConsole will know how to execute it indefinitely.

### Utilize Your Notes for AI Training

Employ your notes to instruct the AI in completing and automating tasks.

### Better than Vector Databases

For each step of your tasks, leverage a precise, efficient, and automated multi-agent Retrieval-Augmented Generation (RAG) system that is on par with expert prompt engineering.

### Completely Open Sourced

This software does not transmit any data to any parties other than the LLM APIs – and you can confirm this for yourself.

### Share Your Tools with the Community

Develop and share your domain-specific AI tools, for instance, on platforms like GitHub or Discord.

## Key aspects

const keyAspects = [
{
title: 'Your Personal AI Universe',
description:
'Construct your own personal AIs, fitted to your bespoke requirements. Spend time on your tool, and watch it grow better and sharper with time.',
btnText: 'Guide me through building my personal assistant using AIConsole.',
},

{
title: 'Teach Your AI New Tricks',
description:
"Make your AI tool adapt over time. Add and manage materials to create a progressively evolving AIConsole that'd serve you even better.",
btnText: 'How does the AI adapt and improve in AIConsole?',
},
{
title: 'Build Domain-Specific Tools',
description:
'Engineer domain tools for the AIConsole, personalizing it to cater to niche tasks and specifications.',
btnText:
'How to develop and customize my domain-specific tools in AIConsole?',
},
{
title: 'Run It Locally',
description:
'Execute AIConsole on your local machine rendering a secure and convenient operation.',
btnText:
"Can you tell me more about running AIConsole locally and it's security aspects?",
},
{
title: 'Learn the Web Interface',
description:
'Navigate through our simplified, user-friendly web interface, that makes your tasks easier to understand and more engaging to complete.',
btnText:
'I would like to know more about the AIConsole web interface, what are its specific features?',
},
{
title: 'Any Task Execution',
description:
'Use AIConsole to automate your work, be it managing your schedule or sending emails.',
btnText:
'Tell me more about how AIConsole executes tasks? what kind of tasks can be executed? what is the spectrum of knowledge AIConsole has access to?',
},
];

## Era of Hyper-Personalisation

I think that not many people talk about one good thing that comes with AI, there are many talks that it will take our jobs, or that it's a treat to humanity.

I belive that AI will actually do the opposity and put the power into the hands of the people.

We are leaving the software area in which big monolith winner takes all startups like Uber or Facebook dominate.

We are entering the area of hyper-personalisation and end user empowerment, which will be all about the power of the individual.

In essence everyone will be running their own LLMs on their own needs and their own data, those AIs will engage with digital world for you.

At 10Clouds AI Labs we have built a tool around those principles, an open source tool called AIConsole.

What AIConsole is?

- A ChatGPT like chatbot, but with multi agent support and ability to craft and store your own pieces of context.
- A desktop application that you can run locally, console can do all the things that you can on your machine.
- An editor that allows you to build and share your domain specfic AI tools (for example on github)
- Describe in plain text how to perform a given task once and then AIConsole knows how to do it forever.
- AIConsole is not based on vector databsase, it maximizes output from AI for each step of your tasks: A precise, efficient and automatic multi-agent RAG system on par with expert prompt engineering.
- With AIConsole you can use plain English to build local, personalized AI tools that will get the job done.

You can check out the test release on https://aiconsole.ai

## How does it work in practice?

Let's say I want to be able to send messages to my girlfriend using AI:

1. Install it using instructions provided here: from github.com/10clouds/aiconsole
2. Creatte a new project directory, for example personal-aiconsole
3. Run aiconsole in that directory
4. Try "Send an imessage to my girlfriend with a my calendar for Today".
5. AIConsole will try to figure out how to do it and most likely fail, due to the fact that it does not know key things: Who is your girlfriends, where is your calendar, how to access it, how to send an imessage.
6. Let's teach it those
7. First create a "Social Circle" material in AIConsole and put there information about who is your girlfriend, if you are on a mac, AIConsole will know how to access your contacts app based on the name provided, but you can also supply full contact information here.
8. Create a "Calendar Manual" material in AIConsole and put there information on where it is located, is it a google calendar local calendar. This will require experimentation as if you will be using local apps you will most likely do not need credentials, and when querying google calendar you will need to provide them along with maybe examples of code that work for it.
   We are currently working on creating a library of materials for common tools, and we want to work with community to build and share those materials.
9. We already have build in imessage manual.
10. Now try to re run the command, it should work. If it stumbles for any reason, reedit the materials, give additional information or instructions and try again.

This way you can teach your AIConsole to do anything for you, you can also provide information about who you are, what you care about, your company services etc so for example it can write blog posts for you or respond in your name, you can provide access to various tools of yours etc.

Looks good but first figure out how to structure those ideas into a blog post because maybe some of those should be put in seperate conceptual "buckets", also besides the philosophical points include in the final blogpost more concrete information on what the current AIConsole provides:

User can create projects for various domains, a book that they are writing, their personal and professional life, a RPG session that they are conducting or central information for accessing their startup data.

In a project a user can create materials: both textual and small snippets of code that helps AIConsole in executing tasks. They can also create agents which specialise in given tasks, like writing content. executing code or giving emotional support.

The system will select the agents and materials needed for a given step of what the user needs.

The user can use this in a similar way they would use ChatGPT but storing in it private data, manipulate their browser, manipulate and extract data from their local files, access apis. While right now it's designed for AI power user, with time it will become more and more accessible as we develop additional features.

Everyone can get it from https://aiconsole.ai

## More info:

- AIConsole can be used as a personal assistant in your various projects.
- AIConsole allows you to build your own AI-Powered, domain specific, multi-agent personal assistant
- AIConsole offers you the ability to add or edit agents and materials. The more you spend time on it, the better it gets.
- AIConsole can be run locally on a user machine
- It can be used to build domain tools
- AI Agents in AIConsole are built in a way that it conserves AI thinking power (context/tokens) so when it executes a complex task it can only use the information (materials and agent speciality) that is needed for that specific subtask.
- AIConsole has a web interface which makes it easy to operate
- AIConsole can execute any task that is doable in python as it generates code and runs it on the fly, this makes it super easy for it to perform tasks like getting your calendar info or sending emails.
- AIConsole does not need you to know coding in order to do that, it executes that code under the hood (but you can still view it).
- AIConsole has multiple agents, all of them having different chracteristics (system prompt) and mode of operation (normal or code execution).
- AIConsole agents will be able to talk to each other and invoke each other (pending, not yet done)
- You can edit and add your own agents, they are in ./agents directory in the directory you run the aiconsole in
- You can provide materials to the agents, those are pieces of information that the agents will select and use during their work, those are (but not limited to): general information about yourself, infromation on how to
  erform a given task like writing a linkedin post, information how to access a given API, information about service offering of your company etc.
- As you add materials and agents this tool grows with power with time. So the more time you spend on it the better it gets. If it does not know how to do a given task you can teach it.
- When you update your installation of aiconsole, make sure to start a fresh project or delete ./materials and ./agents directories in order to get new versions of them with updated materials and agents.
- When you edit a material, it immediatelly gets reloaded and is available in your current conversation
- Create .md files in ./materials directory in the following format:

```md
<!---
Description of when this material should be used?
-->

# Title of the material

Actual content of a material
```

Files are monitored and automatically loaded, then used as context. You can keep there API materials, login information, prompts and other contextual information.

You can see examples of materials i ./materials directory

- You can go back to previous commands using up arrow
- All chats histories are saved in ./chats
- AIConsole is open source, link to repo: https://github.com/10clouds/aiconsole
- 10Clouds (10clouds.com) is developing custom integrations for it, if you need one feel free to contact us.
- Each directory you run it in is your new project directory
- How to run aiconsole:

```shell
pip install --upgrade aiconsole --pre
cd your_project_dir
export OPENAI_API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
aiconsole
```

aiconsole will create a bunch of working files like standard materials and agents

- You have full control how you use the context window of GPT-4, you can delete and edit past messages
- Uses OpenAI GPT-4 internally for all operations, but will be expanded with ability to use open source models. It accesses it through an API.

- Examples of what you can do with AIConsole:

1. Assuming you have description of your company services among your materials, a second material containing top clients and a module to access company org structure (or a text material containing it) - write an email containing a poem about usage of my company services for our top clients and send it to our CTO
2. Write a linkedin post by myself (works really well if you provide it with materials on how to write good linkedin posts, and who are you and what is important to you when talkint with the world)
3. Reject all of my calendar events for tomorrow (assuming you have a material contaning information on how to access your calendar by an API and what are your credentials)

## README

<h2 align="center"><img src="https://github.com/10clouds/aiconsole/assets/135703473/d48b7b40-4b9e-45af-92e4-2abc5a8a40b0" height="64"><br>AIConsole</h2>

<p align="center"><strong>Open Source Desktop Alternative to OpenAI GPTs</strong></p>

# Features

| Feature                             | Description                                                                                                                                                                      |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Run Code Locally                    | Run it locally; the console can perform all the tasks that your machine is capable of executing.                                                                                 |
| Improves with Use                   | Describe in plain text how to perform a given task once, and thereafter AIConsole will know how to execute it indefinitely.                                                      |
| Utilize Your Notes for AI Training  | Employ your notes to instruct the AI in completing and automating tasks.                                                                                                         |
| Better than Vector Databases        | For each step of your tasks, leverage a precise, efficient, and automated multi-agent Retrieval-Augmented Generation (RAG) system that is on par with expert prompt engineering. |
| Completely Open Sourced             | This software does not transmit any data to any parties other than the LLM APIs – and you can confirm this for yourself.                                                         |
| Share Your Tools with the Community | Develop and share your domain-specific AI tools, for instance, on platforms like GitHub or Discord.                                                                              |

# Downloading and Installing

Select the version suitable for your operating system:

- [Windows](https://github.com/10clouds/aiconsole/releases)
- [macOS (Intel)](https://github.com/10clouds/aiconsole/releases)
- [macOS (ARM)](https://github.com/10clouds/aiconsole/releases)
- [Linux](https://github.com/10clouds/aiconsole/releases)

# Basic Flow of Work

Imagine you want to send your daily calendar schedule to your girlfriend through iMessage.

1. Install AIConsole using the instructions provided on GitHub and run it in a new project directory like personal-aiconsole.
2. Input the instruction: "Send an iMessage to my girlfriend with my calendar for today."
3. AIConsole is trying to understand your command, but without knowing who your girlfriend is or access to your calendar, it stumbles.
4. But, every misstep is a learning opportunity. AIConsole uses a concept of materials — user created documents which tell AIConsole how to do stuff, or provide it with contextual information. To teach AIConsole, create a 'Social Circle' material where you include contact information about your girlfriend. In case you're on a macOS, AIConsole will be able to access your Contacts application. But you can also provide the full contact information here
5. Next, within AIConsole create a new material 'Calendar Manual', specifying your calendar's location, whether it's Google Calendar or a local one. This step may require some trial and error as different calendar types may need different kinds of access. In some cases, it might be useful to provide a sample Python code showing how to access your calendar.
6. With our built-in iMessage manual, you are ready to send the message.

After updating these materials, you can retry the step, and provided all the information is accurate, AIConsole will send the iMessage.

# Project Directory Structure

Structure of a project folder

`/` - root directory is added to the python system path, you can place here any custom modules that you want the python interpreter to have access to.

`/agents` - agent .toml files define available agents you can disable and enable them from the app. [example agents](../blob/master/backend/aiconsole/preinstalled/agents)

`/materials` - various materials, notes, manuals and APIs to be injected into GPT context. [examples materials](../blob/master/backend/aiconsole/preinstalled/materials)

`/.aic`

`/settings.toml` - configuration file containing information about disabled materials

Note that in your home app directory you have additional settings.toml which stored global settings.

Material, Agent and settings files are monitored and automatically loaded, then used as context.

# Roadmap

- [x] Initial PIP release
- [x] Switch to GPT-4 Turbo
- [ ] Release of the desktop app for MacOS, Windows and Linux
- [ ] Integrating GPT-V
- [ ] Integrating Dalle-3
- [ ] IDE like experience
- [ ] Handling of non-text materials and files (pdfs etc)
- [ ] Better materials and integrations with various tools
- [ ] Alternative interface to chat for working on a body of text
- [ ] Ability to run on Azure OpenAI Models
- [ ] Ability to run on other models than OpenAI
- [ ] Using AI to modify materials
- [ ] Generative UI
- [ ] Web Hosted SaaS like version

# Contributing

We welcome contributions from the community to make AI Console even better. If you have any ideas, bug reports, or feature requests, please open an issue on the GitHub repository. Feel free to submit pull requests as well!

You can also visit our [Discord channel](https://discord.gg/5hzqZqP4H5) for a further discussion.

# Embedding the AIConsole Backend in Your App

If you want to develop something on top of the aiconsole backend, you may install the backend part using:

`pip install aiconsole`

# Running Development Non-Electron AIConsole

In order to run the non electron development version of AIConsole:

1. To run the standalone backend: `cd backend && poetry install && poetry run dev`
2. To run the standalone frontend: `cd frontend && yarn && yarn dev`

# Buiding the Desktop App

1. To run the development version of electron bundle: `cd electron && yarn dev`
2. To bundle the desktop app: `cd electron && yarn && yarn make`
3. To publish the desktop app: `cd electron && yarn && yarn publish`

# License

AI Console is open-source software licensed under the [Apache License ver. 2.0](https://www.apache.org/licenses/LICENSE-2.0.txt).

# Links

- [Landing page](https://aiconsole.ai)
- [Discord](https://discord.gg/5hzqZqP4H5)
- [Twitter](https://twitter.com/mcielecki)
