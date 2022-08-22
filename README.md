# Organizzed
The purpose of this application is to give users of Slippi a way to properly organize their Slippi replays. 

About:

The purpose of this application is to give users of Slippi to organize their Slippi replays. 

**Organization:**

The File names themselves will be copied and then placed into a Folder.

The idea is to have Folders dedicated to but not limited catergorically by: Players, Match-ups, Specific Days, Wins, Losses, Stage, and Stock Count.

The Copied Files themselves will also be made to be more human readable as opposed to the current method of how they are named.

About:

The purpose of this application is to give users of Slippi to organize their Slippi replays. 

**Organization:**

The File names themselves will be copied and then placed into a Folder.

The idea is to have Folders dedicated to but not limited catergorically by: Players, Match-ups, Specific Days, Wins, Losses, Stage, and Stock Count.

The Copied Files themselves will also be made to be more human readable as opposed to the current method of how they are named.

## Current User Experience looking at Slippi files:


![image](https://res.craft.do/user/full/a9db4317-2a6a-f7ab-117a-91d0db881cfd/doc/7E879A62-C80E-4D95-AFB8-284A9C4D8EB6/4E2EEF41-D6CC-4476-A5B6-46ADC8F0CF2B_2/Ab67JW89DSkCIDxbhArP37kJJMz6QCFebVECDSSWpuMz/Image.png)

Figure: Viewing Slippi Files within Finder

Hmmmmmm… I wonder what these files mean…

I’ll pick…… this one  Game_20210313T183558.slp

One would never be able to decipher what content was inside of this Slippi file unless they were to select it, load it onto the slippi launcher, wait for it to load and then be blessed to see that inside that file is the match between 2Saint and Eddy Mexico that occured on March 13th 2021 where the match-up played was Jigglypuff vs Luigi on Fountain of Dreams that concluded with a victory for 2Saint.

![image](https://res.craft.do/user/full/a9db4317-2a6a-f7ab-117a-91d0db881cfd/doc/7E879A62-C80E-4D95-AFB8-284A9C4D8EB6/C6DF4882-3A3C-4F99-BDE7-5FDF2149CF12_2/1xRyWXxSfxNx2wysBpHvUO7h1QHJyxQqFT63qtqE2Rkz/Image.png)

Figure: Viewing the File within the Slippi Launcher

Now it’s true that the Slippi Launcher already has a way to search individual Slippi files.however that is just about the only thing the launcher can provide. You also would have to do this every single time. You wanted to watch a particular game. Once that happens you might just resort to taking the file copying it and placing it into your own sperate folder already. What if you wanted to send the files for someone else to look at? Nowadays with services like Metafy scnearios such as that is where a file organizer would be an appreciated service.

![image](https://res.craft.do/user/full/a9db4317-2a6a-f7ab-117a-91d0db881cfd/doc/7E879A62-C80E-4D95-AFB8-284A9C4D8EB6/9E800279-8B76-4B77-B676-1AF7B90BCA2B_2/pfeDDVi0PFow4CQR1rHdFx5IkqIe14iAN0aByIJkxqsz/Image.png)

However it cannot even search by character.

So with this tool I aim to develop a way to to get more *organiZZed.*

# Documentation

1. organiZZed will Have a GUI 
2. File Reader: Takes in the file and is able to extract all the data from it
- Input: .slp File
- Output: Date, Time, Players, Match-ups, Specific Days, Wins, Losses, Stage, and Stock Count.
3. object file_properties()

 {

Date,

 Time, 

Players, 

Match-ups, 

Specific Days, 

Wins, Losses, 

Stage, and Stock Count.

}


4. Using the Py-Slippi Parser

-Pip3 install py-slippi
