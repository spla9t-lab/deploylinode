# Guide to Deploying Your Linode Virtual Machine

Welcome to the wild world of cloud computing!

Are you tired of having to waste time waiting for your virtual machine to deploy?
Well, not anymore! With this script, you can deploy your Linode virtual machine with ease.

## Purpose of this Code

This script was created to make your life easier. We all have better things to do than wait for our virtual machines to deploy, and that's where this script comes in. It deploys your Linode virtual machine with the specified image and type, and then periodically checks the status until it's up and running.

## Prerequisites

Before we dive into the code, make sure you have the following:

- A Linode account (duh)
- Your Linode API key (you can find this in the Linode Manager)
- A computer with Python 3.x installed
- The requests library installed (you can install this using `pip install requests`)

## How to Use

Here's what you need to do:

1. Clone this repository onto your computer
2. Open `linode_deployment.py` in your favorite text editor
3. Replace `YOUR_API_KEY` with your actual Linode API key
4. Replace `image` with `linode/ubuntu22.04` and `type` with `g6-nanode-1`
5. Save and close the file
6. Open a terminal window and navigate to the directory where you cloned the repository
7. Run the script by typing `python linode_deployment.py`
8. Sit back, relax, and watch the magic happen
9. Once the script has finished running, check your Linode Manager to make sure your virtual machine has deployed

## Tips and Tricks

- Make sure you have enough funds in your Linode account, or the deployment will fail (awkward)
- You can change the `time_to_wait` variable to make the script check the status more or less often
- If you run into any issues, try checking the response from the Linode API (it's printed in the terminal)

Have fun! Cloud computing is a wild and wacky world, but with this script, you're one step ahead of the game.
Happy deploying!
