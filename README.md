
# CALCULATOR APP

## Description:

Calculator application with the iPhone design built in Python 3.10.6 using MVC (Model View Controller).

## Use:

- Require Python 3.10 to execute it. 

## Structure:


```
     ┏━━━━━━━━┓        ┏━━━━━━━━━━┓        ┏━━━━━━━━┓
     ┃ Model  ┣━━━━━━━━┫Controller┣━━━━━━━━┫  View  ┃
     ┗━━━━━━━━┛       ║┗━━━━━━━━━━┛║       ┗━━━━━━━━┛
                      ║    Main    ║      ● _configure_button_styles
    ● Calculate       ╚════════════╝      ● main
    ● _evaluate       ● main              ● _make_main_frame
 		      ● on_button_click   ● _make_label
		                          ● _make_buttons
                                          ● _is_operator
                                          ● _center_window

```

## Files:

### main.py:

Initiate the app calling the controller main.


### controler.py:

Manage the view and the model of the app.

Instance Model and View class.

main(funcion): call view main function, which execute the GUI render.
on_button_click(function): Send pressed buttons from the model to the view.


### model.py

Initiate `previous_value`: save the value before press next button.
Initiate `value`: the current value.
Initiate `operator`: the operator value.

calculate(function): Conditional list in base which operator was pressed, to apply a determinate mathematic effect.

- caption == 'C': Reset values of `previous_value`, `value`, `operator`.
- caption == '+/-': Add `-` character in 0 position if it don't exist. If exist, remove it.
- caption == '%': Move units to left (nº/100).
- caption == '=': Call `_evaluate` function.
- caption == '.': Create a point if doesn't exist before.
- caption == nº: Add the caption to `value`
- If other case: If exist `value`, `previous_value` = `value` and `operator` = caption. Reset `value`

_evaluate(function): Is called when the caption in calculate = `=`. With `previous_value` and `value` make a mathematic operation with the operator saved.


### view.py

Draw the windows interface for the app.

Initiate `PAD`: with 10 value for padding inside of the screen.
Initiate `MAX_BUTTONS_PER_ROW`: with 4, name of button rows.
Initiate `button_captions`: With tuple of symbols to print it as button characters.

Instance controller.
Initiate title as "PyCalculator 1.0".
Inititate background to black.
Initiate _configure_button_styles, _make_main_frame, _make_label, _make_buttons, _center_window functions.

_configure_button_styles(function): Define different styles for each button type.

main(function): Inititate the Tkinter screen.

_make_main_frame(function): Create a screen and apply the indor padding with `PAD`.

_make_buttons(function): Draw the different buttons with a determinate style in base the button type.

_is_operator(function): Return true if a chart is locatet inside of a tuple. To determinte a type of button.

_center_window(function): Get information about the screen size and place the window in the middle of the screen.



