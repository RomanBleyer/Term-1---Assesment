from terminaltexteffects.effects import effect_print

effect = effect_print.Print("your text here\nwhat are you doooinnnggyour text here\nwhat are you doooinnnggyour text here\nwhat are you doooinnnggyour text here\nwhat are you doooinnnggyour text here\nwhat are you doooinnnggyour text here\nwhat are you doooinnngg")
with effect.terminal_output() as terminal:
    for frame in effect:
        terminal.print(frame)

# notable effects VHSTape
