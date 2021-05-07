# Multiple-Message-Clipboard
A User Interface that allows users to save and copy data on demand against an identifying name.  
  
## Funcitonality  
The User Interface allows for a user to create buttons that, when pressed, copy a message to the user's clipboard.
These messages can be multi-line and are set with an identifying name.
The list of messages is saved when the UI is closed and will be loaded when the user next starts the program.

### 'Add New' Button
The 'Add New' button loads a message box that takes two pieces of information:
* The Identifying Name of the message
* And the Output that will be copied to the users clipboard
The data will not be created, when the Submit button is clicked, as a new 'Message Button' unless both fields are filled in.
Further to this, A user can press the cancel button to destroy the popup if they decide a new button is not necessary.

### Search Function
The search function automatically filters the list of messages by their Identifying names when a user enters the name they are searching for.
This will bring any buttons where the searched name is contained in the Identifying name to be visible.

### Delete Button
Each new button has its own 'Delete' Button.
This will remove the button from the memory of the application so that it can no longer be called.
To ensure this is not done accidentally, the user is prompted with a message to confirm if the user wants to delete the "Identifying Name" button.

### Scrollbar
Whilst not necessary, the Scrollbar allows for a larger number of buttons to be accessed than the size of the interface would allow.
This allows a user to scroll down the list if they need to.

### Saving buttons
Any changes are automatically saved when the application is closed so that users do not lose necessary data they have updated.

## Current Limitations
The user interface is not beautiful, it accomplishes the task of housing the backend.
Users are unable to edit the buttons, they can only delete and create new ones.

## New Updates
None
