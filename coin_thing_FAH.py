import random
import PyQt6.QtWidgets as qtw

def coin_probability(times: int, equal_length: bool = False):

    prob_choices = []
    prob_length_H = []
    prob_length_T = []

    h = 0
    t = 0

    len_T = len(prob_length_T)
    len_H = len(prob_length_H)

    for length in range(times):
        a1 = random.choice(['H', 'T'])
        a2 = random.choice(['H', 'T'])
        a = random.choice([a1, a2])
        
        ap_choices = prob_choices.append(a)

    for letter in prob_choices:
        if letter == 'H':
            h += 1
            prob_length_H.append(h)
        if letter == "T":
            t += 1
            prob_length_T.append(t)

    if prob_length_T == []:
        prob_length_T = [0]
    if prob_length_H == []:
        prob_length_H = [0]
    
    if equal_length:
        while len(prob_length_H) < len(prob_length_T):
            prob_length_H.insert(0, 0)
        while len(prob_length_T) < len(prob_length_H):
            prob_length_T.insert(0, 0)
            
    try:
        percentage2 = round(min(prob_length_H[-1], prob_length_T[-1]) / 
                            max(prob_length_H[-1], prob_length_T[-1]), 2)
    except ZeroDivisionError:
        return [0]
  
    #average = (prob_length_H[-1] + prob_length_T[-1]) / 2

    return percentage2, prob_length_H, prob_length_T, prob_choices


per, h, t, ch = coin_probability(2, False)
print(per)


class dialog_show(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Coin Flip Display")
        self.setFixedSize(500, 1000)

        self.coin()

    def coin(self):
        layout = qtw.QVBoxLayout()

        heads = qtw.QTextBrowser()
        heads.wordWrapMode()
        heads.setText(f'{h}')

        tails = qtw.QTextBrowser()
        tails.wordWrapMode()
        tails.setText(f'{t}')

        layout.addWidget(heads)
        layout.addWidget(tails)
        self.setLayout(layout)

    class coin_order(qtw.QDialog):
        def __init__(self) -> None:
            super().__init__()
            self.setWindowTitle("Coin Order")
            self.setFixedSize(500, 500)
            
            self.move(self.x()+ 1203, self.y())

            self.order()

        def order(self):
            layout = qtw.QVBoxLayout()

            we_all_love_this_order_function = qtw.QTextBrowser()
            we_all_love_this_order_function.wordWrapMode()
            we_all_love_this_order_function.setText(f'{ch}')

            layout.addWidget(we_all_love_this_order_function)
            self.setLayout(layout)

if __name__ == '__main__':
    app = qtw.QApplication([])

    dial = dialog_show()
    dial.show()

    coin = dialog_show.coin_order()
    coin.show()

    app.exec()