# MIT License
#
# Copyright (c) 2024 Khiat Mohammed Abderrezzak
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Author: Khiat Mohammed Abderrezzak <khiat.abderrezzak@gmail.com>

"""Sophisticate Open Confusion Matrix"""

# To Draw The Tables In Console And HTML Code
from tabulate import tabulate
# Data Visualization
from matplotlib.pyplot import imshow, tick_params, axhline, axvline, text, \
    colorbar, xticks, yticks, title, xlabel, ylabel, close, savefig, subplots
# To Open The HTML5 Page
from webbrowser import open as wb


def confusion_matrix(y_or_predicted_y: list, predicted_y_or_y: list) -> list:
    """Confusion Matrix Function"""
    # Checking If The Len > 0
    if len(y_or_predicted_y) > 0:
        # Preparing The Values Counting List
        values = []
        # Concat The Two Lists
        y_and_predicted_y = y_or_predicted_y + predicted_y_or_y
        # Append New Values Into List
        for i in range(len(y_and_predicted_y)):
            if y_and_predicted_y[i] not in values:
                values.append(y_and_predicted_y[i])
        # Sorting The List
        values = sorted(values)
        # Preparing The Confusion Matrix
        confMat = [[0 for _ in values] for _ in values]
        # Counting
        for i in range(len(y_or_predicted_y)):
            confMat[values.index(y_or_predicted_y[i])
                    ][values.index(predicted_y_or_y[i])] += 1
        # Return Confusion Matrix And Values
        return confMat, values
    else:
        # Return Empty Confusion Matrix And None Values
        return [], None


def imshow_config(cm: list, val: list = [], html: bool = False, detail: bool = True) -> None:
    """Imshow Function"""
    if not html:
        # Preparing Imshow
        imshow(cm, interpolation='nearest', cmap="Paired")  # Or Accent
        # Puting The XLabel
        title(
            "Predicted Classes" if len(cm) > 1 else "Predicted Class", fontsize=10, loc="center")
        # Puting The Imshow ColorBar
        colorbar()
        # Changing The X Axis And Y Axis Places
        tick_params(axis='x', which='both', bottom=False,
                    top=False, labeltop=True, labelbottom=False)
        tick_params(axis='y', which='both', left=False,
                    right=False, labelright=False, labelleft=True)
        # Printing The Title And YLabel
        xlabel("\nConfusion Matrix (Unary Classification)" if len(
            cm) == 1 else "\nConfusion Matrix (Binary Classification)" if len(cm) == 2 else "\nConfusion Matrix (Multi Classification)", loc="center")
        ylabel("Actual Classes" if len(cm) >
               1 else "Actual class", loc="center")
        # Deviding Imshow Squares With Black Bold Lines
        if len(cm) > 1:
            for i in range(1, len(val)):
                # Horizontal Line
                axhline(i - 0.5, color='black',
                        linewidth=2)
                # Vertical Line
                axvline(i - 0.5, color='black',
                        linewidth=2)
    else:
        # Size Up The Imshow Window
        fig, ax = subplots(figsize=(10, 8))
        # Preparing The Imshow
        plot_conf_mat(conf_mat=cm, classes_names=val, detail=detail)
        # Saving The Imshow File (Img) Png Format
        savefig("conf_mat.png", format="png")
        # Closing The Window Of Imshow
        close()


def label_encoder(y_or_predicted_y: list, isint1: bool, predicted_y_or_y: list, isint2: bool) -> list:
    """Label Encoder Function"""
    # If The First List Not Contain Int Values And The Second List Contain Int Values
    if not isint1 and isint2:
        # Preparing The Values Counting Lists
        target = []
        mining = []
        # Append New Values Into Lists
        for value in y_or_predicted_y:
            if value not in mining:
                mining.append(value)
        for value in predicted_y_or_y:
            if value not in target:
                target.append(value)
        # Converting Two Lists Values To Str Data Type If Not
        target = list(map(str, target))
        mining = list(map(str, mining))
        # Sorting The Two Lists
        target.sort()
        mining = sorted(mining)
        # Fix The Difference Between The Two Lists
        if len(mining) > len(target):
            dif = len(mining) - len(target)
            for i in range(dif):
                target.append(len(target)+i)
        # Label Encoding
        for i in range(len(y_or_predicted_y)):
            y_or_predicted_y[i] = target[mining.index(
                str(y_or_predicted_y[i]))]
        # Preparing X Axis And Y Axis Real Values List
        final = []
        # Append The Real Values In X Axis And Y Axis List
        for i, j in zip(mining, target):
            final.append(i+"/"+j)
        # Return Encoded Data
        return y_or_predicted_y, list(map(str, predicted_y_or_y)), final
    # If The First List Contain Int Values And The Second List Not Contain Int Values
    elif isint1 and not isint2:
        # Preparing The Values Counting Lists
        target = []
        mining = []
        # Append New Values Into Lists
        for value in y_or_predicted_y:
            if value not in target:
                target.append(value)
        for value in predicted_y_or_y:
            if value not in mining:
                mining.append(value)
        # Converting Two Lists Values To Str Data Type If Not
        target = list(map(str, target))
        mining = list(map(str, mining))
        # Sorting The Two Lists
        target.sort()
        mining = sorted(mining)
        # Fix The Difference Between The Two Lists
        if len(mining) > len(target):
            dif = len(mining) - len(target)
            for i in range(dif):
                target.append(len(target)+i)
        # Label Encoding
        for i in range(len(predicted_y_or_y)):
            predicted_y_or_y[i] = target[mining.index(
                str(predicted_y_or_y[i]))]
        # Preparing X Axis And Y Axis Real Values List
        final = []
        # Append The Real Values In X Axis And Y Axis List
        for i, j in zip(target, mining):
            final.append(i+"/"+j)
        # Return Encoded Data
        return list(map(str, y_or_predicted_y)), predicted_y_or_y, final
    # If The Two Lists Not Contain Int Values
    else:
        # Preparing The Values Counting List
        counter = []
        # Concat The Two Lists
        y_and_predicted_y = y_or_predicted_y + predicted_y_or_y
        # Changing The Types Of Values To Str If Not
        y_and_predicted_y = list(map(str, y_and_predicted_y))
        # Append New Values Into List
        for value in y_and_predicted_y:
            if value not in counter:
                counter.append(value)
        # Sorting The List
        counter.sort()
        # Encode The First List
        for i in range(len(y_or_predicted_y)):
            y_or_predicted_y[i] = counter.index(str(y_or_predicted_y[i]))
        # Encode The Second List
        for i in range(len(predicted_y_or_y)):
            predicted_y_or_y[i] = counter.index(str(predicted_y_or_y[i]))
        # Return Encoded Data
        return y_or_predicted_y, predicted_y_or_y, counter


def check_one(predicted_y_or_y: list) -> bool:
    """Check-One Function"""
    # Check For Numpy Or Torch Data Types
    numpy_torch_data_types = ["<class 'numpy.int8'>", "<class 'numpy.uint8'>",
                              "<class 'numpy.int16'>", "<class 'numpy.uint16'>", "<class 'numpy.int32'>", "<class 'numpy.uint32'>", "<class 'numpy.int64'>", "<class 'numpy.uint64'>", "<class 'torch.Tensor'>"]
    if str(type(predicted_y_or_y[0])) in numpy_torch_data_types:
        return True


def check_two(predicted_y_or_y: list) -> bool:
    """Check-Two Function"""
    # Check For TensorFlow Data Types
    tensorflow_data_types = ["int8", "int16", "int32", "int64"]
    for type in tensorflow_data_types:
        if type in str(predicted_y_or_y[0]):
            return True


def check_type(predicted_y_or_y: list) -> bool:
    """Check Type Function"""
    # Check In Check-One Function
    if check_one(predicted_y_or_y):
        return True
    # Check In Check-Two Function
    elif check_two(predicted_y_or_y):
        return True
    else:
        # Check For Int Or Another Data Types
        for value in predicted_y_or_y:
            # Checking If Each Value Is Not Valid
            if type(value) != int:
                return False
            # Checking If Each Value Is Valid
            else:
                continue
        return True


def normalize(cm: list) -> list:
    """Normalize Function"""
    # Copying The Values Into A New List
    rcm = [[cm[i][j] for j in range(len(cm[i]))] for i in range(len(cm))]
    for lines in range(len(rcm)-1):
        for columns in range(len(rcm[lines])):
            # Reverse The Two Diagonal
            help = rcm[lines][columns]
            rcm[lines][columns] = rcm[1 - lines][1-columns]
            rcm[1-lines][1-columns] = help
    return rcm


def red(text: str) -> str:
    """Red Coloring Function"""
    # Coloring The Input Text With Red Color
    return "\033[91;1m{}\033[00m".format(text)


def green(text: str) -> str:
    """Green Coloring Function"""
    # Coloring The Input Text With Green Color
    return "\033[92;1m{}\033[00m".format(text)


def yellow(text: str) -> str:
    """Yellow Coloring Function"""
    # Coloring The Input Text With Yellow Color
    return "\033[93;1m{}\033[00m".format(text)


def blue(text: str) -> str:
    """Blue Coloring Function"""
    # Coloring The Input Text With Blue Color
    return "\033[94;1m{}\033[00m".format(text)


def classification_report_calculation(cm: list, val: list = [], html: bool = False) -> float | list:
    """Classification Report Calculation"""
    if len(cm) == 2:
        # Calculating The Accuracy Rate
        accuracy = (cm[1][1] + cm[0][0]) / \
            (cm[1][1] + cm[0][0] + cm[1][0] + cm[0][1])
        # Calculating The Error Rate
        error = round(1-accuracy, 2)
        # Percesion Calculation
        try:
            precision = cm[1][1] / (cm[1][1] + cm[0][1])
        except ZeroDivisionError as e1:
            precision = float(1)
        try:
            negative_precision = cm[0][0]/(cm[1][0]+cm[0][0])
        except ZeroDivisionError as e2:
            negative_precision = float(1)
        # Recall Calculation
        try:
            recall = cm[1][1] / (cm[1][1] + cm[1][0])
        except ZeroDivisionError as e3:
            recall = float(1)
        try:
            specificity = cm[0][0]/(cm[0][0]+cm[0][1])
        except ZeroDivisionError as e4:
            specificity = float(1)
        # Support Calculation
        support_1 = cm[1][0] + cm[1][1]
        support_0 = cm[0][1] + cm[0][0]
        # F1-Score Calculation
        try:
            f_score_1 = (2 * precision * recall) / (precision + recall)
        except ZeroDivisionError as e5:
            f_score_1 = float(0)
        try:
            f_score_0 = (2 * negative_precision * specificity) / \
                (negative_precision + specificity)
        except ZeroDivisionError as e6:
            f_score_0 = float(0)
        return accuracy, error, precision, negative_precision, recall, specificity, support_1, support_0, f_score_1, f_score_0
    elif len(cm) > 2:
        # All Values Sum (Correct And Wrong)
        total = 0
        # Preparing The Classification Report Matrix.
        class_repo = [[0 for _ in range(4)] for _ in range(len(val))]
        # Percesion Sum
        per_sum = 0
        # Recall Sum
        rec_sum = 0
        # F1-Score Sum
        f1_sum = 0
        # Weighted Avg
        wa_per_sum = 0
        wa_rec_sum = 0
        wa_f1_sum = 0
        # Preparing The Classification Report Matrix Content
        for i in range(len(class_repo)):
            # Column Sum
            col_sum = 0
            for j in range(len(cm)):
                # Increase In The Column Sum
                col_sum += cm[j][i]
                # Increase In The Total Sum
                total += cm[j][i]
            # Precision Calculation
            if col_sum == 0:
                class_repo[i][0] = float(1)
            else:
                class_repo[i][0] = cm[i][i]/col_sum
            # Increase In The Percesion Sum
            per_sum += class_repo[i][0]
            # Recall Calculation
            som1 = sum(cm[i])
            if som1 == 0:
                class_repo[i][1] = float(1)
            else:
                class_repo[i][1] = cm[i][i]/sum(cm[i])
            # Increase In The Recall Sum
            rec_sum += class_repo[i][1]
            # F1-Score Calculation
            som2 = class_repo[i][0]+class_repo[i][1]
            if som2 == 0:
                class_repo[i][2] = float(0)
            else:
                class_repo[i][2] = (
                    (2*class_repo[i][0]*class_repo[i][1])/som2)
            # Increase In The F1-Score Sum
            f1_sum += class_repo[i][2]
            # Support Calculation
            class_repo[i][3] = sum(cm[i])
            # Calculating Percesion For The Weighted Avg
            wa_per_sum += class_repo[i][0] * class_repo[i][3]
            # Calculating Recall For The Weighted Avg
            wa_rec_sum += class_repo[i][1] * class_repo[i][3]
            # Calculating F1-Score For The Weighted Avg
            wa_f1_sum += class_repo[i][2] * class_repo[i][3]
            # Round The Precision Value
            class_repo[i][0] = round(class_repo[i][0], 2)
            # Round The Precision Value
            class_repo[i][1] = round(class_repo[i][1], 2)
            # Round The F1-Score Value
            class_repo[i][2] = round(class_repo[i][2], 2)
        # Preparing The Macro Avg And Weighted Avg Matrix.
        class_repo_con = [["Macro Avg", round(per_sum/len(val), 2), round(rec_sum/len(val), 2), round(f1_sum/len(val), 2), total], ["Weighted Avg",
                                                                                                                                    round(wa_per_sum/total, 2), round(wa_rec_sum/total, 2), round(wa_f1_sum/total, 2), total]]
        # Correct Values Sum
        correct = 0
        # Wrong Values Sum
        wrong = 0
        # Colored The Values
        for i in range(len(cm)):
            for j in range(len(cm[i])):
                if i == j:
                    if cm[i][j] != 0:
                        # Increase In The Correct Values Sum
                        correct += cm[i][j]
                        # Colored The Correct Values (Not None)
                        if not html:
                            cm[i][j] = yellow(
                                cm[i][j])
                    else:
                        # Colored The Correct Values (None)
                        if not html:
                            cm[i][j] = green(
                                cm[i][j])
                else:
                    if cm[i][j] != 0:
                        # Increase In The Wrong Values Sum
                        wrong += cm[i][j]
                        # Colored The Wrong Values (Not None)
                        if not html:
                            cm[i][j] = red(cm[i][j])
                    else:
                        # Colored The Wrong Values (None)
                        if not html:
                            cm[i][j] = blue(
                                cm[i][j])
        # Calculating The Accuracy Rate
        accuracy = correct / total
        # Calculating The Error Rate
        error = wrong / total
        # Insert The Column Of Classes
        val.insert(0, "Classes")
        # Insert Classes In Confusion Matrix
        for i in range(len(cm)):
            cm[i].insert(0, val[i+1])
        # Insert Classes In Classification Report Matrix
        for i in range(len(class_repo)):
            class_repo[i].insert(0, val[i+1])
        return accuracy, error, class_repo, class_repo_con
    else:
        # Printing Error Msg
        print("This Function Work Just With Confusion Matrix of Length >= 2")


def classes_check(classes_names: list, val: list, func: int) -> list:
    """Classes Names Check Function"""
    # Check The Type Of Classes Names variable
    if type(classes_names) == list:
        if len(classes_names) == 0:
            # Keeping The Default List
            return val
        elif len(classes_names) != 0 and (len(classes_names) > len(val) or len(classes_names) < len(val)):
            # Printing Error Msg
            print(
                ("conf_mat_to_html " if func == 2 else "print_conf_mat " if func == 1 else "plot_conf_mat ") + red("Warning") + " : The Number Of Classes Names Is Different From The Number Of Classes")
            return val
        else:
            # Update To The New List
            return classes_names
    elif type(classes_names) == dict:
        l = list(classes_names)
        for i, j in classes_names.items():
            if type(j) == int:
                try:
                    l[j] = i
                except IndexError as e1:
                    classes_names = list(classes_names)
                    break
            else:
                for i, j in classes_names.items():
                    if type(i) == int:
                        try:
                            l[i] = j
                        except IndexError as e2:
                            classes_names = list(
                                classes_names.values())
                            break
                    else:
                        classes_names = list(classes_names)
                        break
                else:
                    classes_names = l
                break
        else:
            classes_names = l
        if len(classes_names) == len(val):
            return classes_names
        else:
            # Printing Error Msg
            print(
                ("conf_mat_to_html " if func == 2 else "print_conf_mat " if func == 1 else "plot_conf_mat ") + red("Warning") + " : The Number Of Classes Names Is Different From The Number Of Classes")
            return val
    else:
        try:
            # Converting The Classes Names List Into List Type
            classes_names = list(classes_names)
        except:
            # Converting The Classes Names List Into List Type After Str Type
            classes_names = list(str(classes_names))
        if len(classes_names) == len(val):
            # Update To The New List
            return classes_names
        else:
            # Printing Error Msg
            print(
                ("conf_mat_to_html " if func == 2 else "print_conf_mat " if func == 1 else "plot_conf_mat ") + red("Warning") + " : The Number Of Classes Names Is Different From The Number Of Classes")
            return val


def control(y_or_predicted_y: list, predicted_y_or_y: list, classes_names: list = [], func: int = -1, spe: bool = False) -> list:
    """Control Function"""
    # Changing The Type Of Column Into A List If Not
    if type(y_or_predicted_y) != list:
        y_or_predicted_y = list(y_or_predicted_y)
    if type(predicted_y_or_y) != list:
        predicted_y_or_y = list(predicted_y_or_y)
    # Check The Type For All Data Inside The List
    y_t = check_type(y_or_predicted_y)
    y_p = check_type(predicted_y_or_y)
    if not y_t or not y_p:
        # Label Encoding For Non int Data
        y_or_predicted_y, predicted_y_or_y, valu = label_encoder(
            y_or_predicted_y, y_t, predicted_y_or_y, y_p)
        # Confusion Matrix Calculation
        cm, val = confusion_matrix(y_or_predicted_y, predicted_y_or_y)
        if spe != True:
            val = classes_check(classes_names, valu, func)
    else:
        # Confusion Matrix Calculation
        cm, val = confusion_matrix(y_or_predicted_y, predicted_y_or_y)
        if spe != True:
            val = classes_check(classes_names, val, func)
    return cm, val


def calc_conf_mat(y_or_predicted_y: list, predicted_y_or_y: list) -> list:
    """Confusion Matrix Calculation Function"""
    if len(y_or_predicted_y) == len(predicted_y_or_y):
        cm, val = control(y_or_predicted_y,
                          predicted_y_or_y, spe=True)
    else:
        # Printing Error Msg
        print(
            "The List Of Original Values And The List Of Predicted Values Are Not Of The Same Length :(\n")
    return cm


def plot_conf_mat(y_or_predicted_y: list = [], predicted_y_or_y: list = [], *, classes_names: list = [], conf_mat: list = [], detail: bool = True) -> None:
    """Confusion Matrix Graphic Display Function"""
    # check The Len Of Two Lists
    if len(y_or_predicted_y) == len(predicted_y_or_y):
        if len(conf_mat) == 0:
            # Calculating The Confusion Matrix
            cm, val = control(y_or_predicted_y,
                              predicted_y_or_y, classes_names, 0)
        else:
            # Puting The Confusion Matrix Directely
            cm = list(conf_mat)
            # Checking The Classes Names
            val = classes_check(classes_names, [*range(len(cm))], 0)
        if len(cm) == 0:
            # Printing Msg
            print("There Is Nothing To See Here :)\n")
        elif len(cm) == 1:
            # Preparing Imshow
            imshow_config(cm)
            # Printing The Real Values In X Axis And Y Axis
            xticks(ticks=[0], labels=[
                f"Positive If Pos OR Negative If Neg ({val[0]})"])
            yticks(ticks=[0], labels=[
                f"Pos OR Neg ({val[0]})"], rotation=90)
            # Preparing The Data Of Square
            annot = [
                f"True Positive OR True Negative \n\nTP OR TN : \n\n{cm[0][0]}"] if detail else [cm[0][0]]
            # Printing The Data Into Square
            text(0, 0, f'{annot[0]}', horizontalalignment='center',
                 verticalalignment='center', fontsize=10, color='black')
        elif len(cm) == 2:
            # Reverse The Confusion Matrix
            rcm = normalize(cm)
            # Preparing Imshow
            imshow_config(rcm, val)
            # Printing The Real Values In X Axis And Y Axis
            xticks(ticks=[0, 1], labels=[
                f"Positive ({val[1]})", f"Negative ({val[0]})"])
            yticks(ticks=[0, 1], labels=[
                f"Pos ({val[1]})", f"Neg ({val[0]})"], rotation=0)
            # Preparing The Data Of Each Square
            annot = [[f"True Positive (TP) :\n\n{cm[1][1]}", f"Type II Error (Missed)\n\nFalse Negative (FN) :\n\n{cm[1][0]}"], [
                f"Type I Error (Wrong)\n\nFalse Positive (FP) :\n\n{cm[0][1]}", f"True Negative (TN) :\n\n{cm[0][0]}"]] if detail else [[cm[1][1], cm[1][0]], [
                    cm[0][1], cm[0][0]]]
            # Printing The Data Into Each Square Of Imshow
            for i in range(len(val)):
                for j in range(len(val)):
                    text(j, i, f'{annot[i][j]}', horizontalalignment='center',
                         verticalalignment='center', fontsize=10, color='black')
        else:
            # Preparing Imshow
            imshow_config(cm, val)
            # Printing The Real Values In X Axis And Y Axis
            xticks(ticks=[*range(len(val))], labels=val)
            yticks(ticks=[*range(len(val))], labels=val, rotation=0)
            # Printing The Data Into Each Square Of Imshow
            for i in range(len(val)):
                for j in range(len(val)):
                    text(j, i, f'{cm[i][j]}', horizontalalignment='center',
                         verticalalignment='center', fontsize=10, color='black')
    else:
        # Printing Error Msg
        print(
            "The List Of Original Values And The List Of Predicted Values Are Not Of The Same Length :(\n")


def print_conf_mat(y_or_predicted_y: list, predicted_y_or_y: list, *, classes_names: list = [], detail: bool = True) -> list:
    """Confusion Matrix Display Function"""
    # check The Len Of Two Lists
    if len(y_or_predicted_y) == len(predicted_y_or_y):
        cm, val = control(y_or_predicted_y, predicted_y_or_y, classes_names, 1)
        cmc = [[cm[i][j] for j in range(len(cm[i]))]
               for i in range(len(cm))]
        if len(cm) == 0:
            # Printing All Data
            print([])
        if len(cm) == 1:
            # Preparing Confusion Matrix
            data1 = [
                [
                    "",
                    f"Positive If Positive OR Negative If Negative ({val[0]})",
                ],
                [
                    f"Positive OR Negative ({val[0]})",
                    f"True Positive OR True Negative \n\n           TP OR TN : \n\n              {cm[0][0]}" if detail else cm[
                        0][0],
                ],
            ]
            # Preparing The Rate/Score Table
            data2 = [
                [
                    "",
                    "Rate (Score)",
                ],
                [
                    "Accuracy",
                    "1",
                ],
                [
                    "Error",
                    "0",
                ],
            ]
            # Preparing Classification Report
            data3 = [
                [
                    "Precision (P)",
                    "Recall (R)",
                    "F1-Score (F)",
                    "Support (S)",
                ],
                [
                    f"Positive OR Negative ({val[0]})",
                    "1",
                    "1",
                    "1",
                    f"{cm[0][0]}",
                ],
                [
                    "Macro Avg",
                    "1",
                    "1",
                    "1",
                    f"{cm[0][0]}",
                ],
                [
                    "Weighted Avg",
                    "1",
                    "1",
                    "1",
                    f"{cm[0][0]}",
                ],
            ]
            # Printing All Data
            print("\nConfusion Matrix : \n" + "_" *
                  len("Confusion Matrix") + "\n")
            print(tabulate(data1, headers="firstrow",
                           tablefmt="fancy_grid") + "\n")
            print(tabulate(data2, headers="firstrow",
                           tablefmt="fancy_grid") + "\n")
            print("\nClassification Report : \n" + "_" *
                  len("Classification Report") + "\n")
            print(tabulate(data3, headers="firstrow", tablefmt="fancy_grid"))
        elif len(cm) == 2:
            accuracy, error, precision, negative_precision, recall, specificity, support_1, support_0, f_score_1, f_score_0 = classification_report_calculation(
                cm)
            # Preparing Confusion Matrix
            data1 = [
                [
                    "Classes",
                    "Predicted Positive (PP)",
                    "Predicted Negative (PN)",
                    "",
                ],
                [
                    "Actual Positive (P)",
                    ("True Positive (" + yellow("TP") +
                     f") : {cm[1][1]}") if detail else cm[1][1],
                    ("False Negative (" + blue("FN") +
                     f") : {cm[1][0]}\nType II Error (Missed)") if detail else cm[1][0],
                ],
                [
                    "Actual Negative (N)",
                    ("False Positive (" + red("FP") +
                     f") : {cm[0][1]}\nType I Error (Wrong)") if detail else cm[0][1],
                    ("True Negative (" + green("TN") +
                     f") : {cm[0][0]}") if detail else cm[0][0],
                ],
            ]
            # Preparing The Rate/Score Table
            data2 = [
                [
                    "",
                    "Rate (Score)",
                ],
                [
                    "Accuracy",
                    ("Correct        " + yellow("TP") + " + " + green("TN") + "\n" + "_" * len("Correct") + " : " + "_" *
                     len("TP + FP + FN + TN") + "  OR  1 - Error " + " =  " +
                     f"{round(accuracy, 2)}" +
                     "\n\n Total    " +
                     yellow("TP") + " + " + red("FP") + " + " +
                     blue("FN") + " + " +
                     green("TN")) if detail else round(accuracy, 2),
                ],
                [
                    "Error",
                    ("Wrong        " + red("FP") + " + " + blue("FN") + "\n" + "_" * len("Wrong") + " : " + "_" *
                     len("TP + FP + FN + TN") + "  OR  1 - Accuracy " +
                     " =  " + f"{error}" + "\n\nTotal   " + yellow("TP") + " + " + red(
                        "FP") + " + " + blue("FN") + " + " + green("TN")) if detail else error,
                ],
            ]
            # Preparing Classification Report
            data3 = [
                [
                    "Precision (P)",
                    "Recall (R)",
                    "F1-Score (F)",
                    "Support (S)",
                ],
                [
                    f"Positive ({val[1]})",
                    ("P1 (PPV): \n\n  " + yellow("TP") + "\n" + "_" *
                     len("TP + FP") + "  = " +
                     f"{round(precision, 2)}" + "\n\n" + yellow("TP") +
                     " + " + red("FP")) if detail else round(precision, 2),
                    (f"R1 (Sensitivity):\n\n  " + yellow("TP") + "\n" + "_" * len("TP + FN") +
                     "  = " + f"{round(recall, 2)}" + "\n\n" + yellow("TP") +
                     " + " + blue("FN")) if detail else round(recall, 2),
                    ("F1 : \n\n" + "2 x P1 x R1\n" + "_" * len("2 x P1 x R1") +
                     "  = " + f"{round(f_score_1, 2)}" + "\n\n  P1 + R1") if detail else round(f_score_1, 2),
                    ("S1 : \n\n\n " + yellow("TP") + " + " +
                     blue("FN") + f" = {support_1}") if detail else support_1,
                ],
                [
                    f"Negative ({val[0]})",
                    (f"P0 (NPV): \n\n  " + green("TN") + "\n" + "_" *
                     len("TN + FN") + "  = " +
                     f"{round(negative_precision, 2)}" +
                     "\n\n" +
                     green("TN") + " + " +
                     blue("FN")) if detail else round(negative_precision, 2),
                    (f"R0 (Specificity): \n\n  " + green("TN") + "\n" + "_" * len("TN + FP") +
                     "  = " + f"{round(specificity, 2)}" +
                     "\n\n" + green("TN") + " + " +
                     red("FP")) if detail else round(specificity, 2),
                    ("F0 : \n\n" + "2 x P0 x R0\n" + "_" * len("2 x P0 x R0") +
                     "  = " + f"{round(f_score_0, 2)}" + "\n\n  P0 + R0") if detail else round(f_score_0, 2),
                    ("S0 : \n\n\n " + red("FP") + " + " + green(
                        "TN") + f" = {support_0}") if detail else support_0,
                ],
                [
                    "Macro Avg",
                    ("P1 + P0\n" + "_" *
                     len("P1 + P0") + "  = " +
                     f"{round((precision + negative_precision)/2, 2)}" +
                     "\n\n   2") if detail else round((precision + negative_precision)/2, 2),
                    ("R1 + R0\n" + "_" *
                     len("R1 + R0") + "  = " +
                     f"{round((recall + specificity)/2, 2)}" + "\n\n   2") if detail else round((recall + specificity)/2, 2),
                    ("F1 + F0\n" + "_" * len("F1 + F0") + "  = " +
                     f"{round((f_score_1 + f_score_0)/2, 2)}" + "\n\n   2") if detail else round((f_score_1 + f_score_0)/2, 2),
                    (f"TS = {support_0 + support_1}") if detail else support_0 + support_1,
                ],
                [
                    "Weighted Avg",
                    ("W1\n" + "_" * len("TS") + "  = " +
                     f"{round(((precision * support_1) + (negative_precision * support_0))/(support_0 + support_1), 2)}" + "\n\nTS") if detail else round(((precision * support_1) + (negative_precision * support_0))/(support_0 + support_1), 2),
                    ("W2\n" + "_" * len("TS") + "  = " +
                     f"{round(((recall * support_1) + (specificity * support_0))/(support_0 + support_1), 2)}" + "\n\nTS") if detail else round(((recall * support_1) + (specificity * support_0))/(support_0 + support_1), 2),
                    ("W3\n" + "_" * len("TS") + "  = " +
                     f"{round(((f_score_1 * support_1) + (f_score_0 * support_0))/(support_1 + support_0),2)}" + "\n\nTS") if detail else round(((f_score_1 * support_1) + (f_score_0 * support_0))/(support_1 + support_0), 2),
                    (f"TS = {support_0 + support_1}") if detail else support_0 + support_1,
                ],
            ]
            # Printing All Data
            print("\nConfusion Matrix : \n" + "_" *
                  len("Confusion Matrix") + "\n")
            print(tabulate(data1, headers="firstrow",
                           tablefmt="fancy_grid") + "\n")
            print(tabulate(data2, headers="firstrow",
                           tablefmt="fancy_grid") + "\n")
            print("\nClassification Report : \n" + "_" *
                  len("Classification Report") + "\n")
            print(tabulate(data3, headers="firstrow", tablefmt="fancy_grid"))
            if detail:
                print("\nPPV : Positive Predictive Value")
                print("\nNPV : Negative Predictive Value")
                print("\nW1 = (P1 x S1) + (P0 x S0)")
                print("\nW2 = (R1 x S1) + (R0 x S0)")
                print("\nW3 = (F1 x S1) + (F0 x S0)")
                print("\nTS : Total Support = S1 + S0")
                print(
                    "\nNote : All Real Numbers Are Rounded With Two Digits After The Comma\n")
        else:
            accuracy, error, class_repo, class_repo_con = classification_report_calculation(
                cm, val)
            # Concat The Classes with Confusion Matrix
            data1 = [val] + cm
            # Preparing The Rate/Score Table
            data2 = [
                [
                    "",
                    "Rate (Score)",
                ],
                [
                    "Accuracy",
                    ("Correct      " + "Sum Of " + yellow("Yellow") + " Values\n" + "_" * len("Correct") + " : " + "_" *
                     len("Sum Of Yellow And Red Values") + "  OR  1 - Error " + " =  " +
                     f"{round(accuracy, 2)}" +
                     "\n\n Total    Sum Of " +
                     yellow("Yellow")+" And " + red("Red")+" Values") if detail else round(accuracy, 2),
                ],
                [
                    "Error",
                    ("Wrong        " + "Sum Of " + red("Red") + " Values\n" + "_" * len("Wrong") + " : " + "_" *
                     len("Sum Of Yellow And Red Values") + "  OR  1 - Accuracy " + " =  " +
                     f"{round(error, 2)}" +
                     "\n\nTotal   Sum Of " +
                     yellow("Yellow")+" And " + red("Red") + " Values") if detail else round(error, 2),
                ],
            ]
            # Concat The header Row With The Classification Report Matrix
            data3 = [["", "Precision (P)", "Recall (R)",
                      "F1-Score (F)", "Support (S)"]] + class_repo + class_repo_con
            # Printing All Data
            print("\nConfusion Matrix : \n" + "_" *
                  len("Confusion Matrix") + "\n")
            print(tabulate(data1, headers="firstrow",
                           tablefmt="fancy_grid") + "\n")
            if detail:
                print(yellow("Yellow"), end=" ")
                print(
                    " : Not None Correct Values / True Positive (TP) OR True Negative (TN)")
                print(red("Red"), end=" ")
                print(
                    "    : Not None Wrong Values / False Positive (FP) OR False Negative (FN)")
                print(green("Green"), end=" ")
                print("  : None Correct Values")
                print(blue("Blue"), end=" ")
                print("   : None Wrong Values\n")
            print(tabulate(data2, headers="firstrow",
                           tablefmt="fancy_grid") + "\n")
            print("\nClassification Report : \n" + "_" *
                  len("Classification Report") + "\n")
            print(tabulate(data3, headers="firstrow",
                           tablefmt="fancy_grid") + "\n")
            if detail:
                print("Precision    : " + yellow("Yellow") +
                      " Value / Sum Of " + yellow("Yellow") + " Value Column\n")
                print("Recall       : " + yellow("Yellow") + " Value / Sum Of " +
                      yellow("Yellow") + " Value Row\n")
                print("F1-Score     : (2 x Precision x Recall) / (Precision + Recall)\n")
                print("Support      : Sum Of Each Row\n")
                print("Macro Avg    :\n")
                print(
                    "               Precision : (Sum Of Precision Column) / Classes Count\n")
                print(
                    "               Recall    : (Sum Of Recall Column) / Classes Count\n")
                print(
                    "               F1-Score  : (Sum Of F1-Score Column) / Classes Count\n")
                print("               Support   : Total (Sum Of All Matrix)\n")
                print("Weighted Avg :\n")
                print(
                    "               Precision : (Sum Of (Precision x support)) / Total (Sum Of All Matrix)\n")
                print(
                    "               Recall    : (Sum Of (Recall x Support)) / Total (Sum Of All Matrix)\n")
                print(
                    "               F1-Score  : (Sum Of (F1-Score x Support)) / Total (Sum Of All Matrix)\n")
                print("               Support   : Total (Sum Of All Matrix)\n")
                print(
                    "Note : All Real Numbers Are Rounded With Two Digits After The Comma\n")
        return cmc
    else:
        # Printing Error Msg
        print(
            "The List Of Original Values And The List Of Predicted Values Are Not Of The Same Length :(\n")


def update_html(void: None = None) -> None:
    """HTML Code Update Function"""
    with open("conf_mat.html", "r") as file:
        # Reading The File Line By Line And Seting Him Into A List
        lines = file.readlines()
        for i in range(len(lines)):
            if lines[i] == "<table>\n":
                # Add border=1
                lines[i] = "<table border=1>\n"
    with open("conf_mat.html", "w") as file:
        # Writing New And Missing HTML Code
        file.write("<!DOCTYPE html>\n")
        file.write('<html lang="en">\n\n')
        file.write("<head>\n")
        file.write('<meta charset="UTF-8">\n')
        file.write(
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        file.write("<title>conf_mat</title>\n")
        file.write("</head>\n")
        file.write("<body>\n")
        file.writelines(lines)
        file.write("</body>\n")
        file.write("</html>")


def conf_mat_to_html(y_or_predicted_y: list = [], predicted_y_or_y: list = [], *, classes_names: list = [], conf_mat: list = [], detail: bool = True) -> None:
    """Confusion Matrix Display/Graphic Display Function (All In One HTML Page)"""
    # check The Len Of Two Lists
    if len(y_or_predicted_y) == len(predicted_y_or_y):
        if len(conf_mat) == 0:
            # Calculating The Confusion Matrix
            cm, val = control(y_or_predicted_y,
                              predicted_y_or_y, classes_names, 2)
        else:
            # Puting The Confusion Matrix Directely
            cm = list(conf_mat)
            # Converting The Rows Into A List Data Type
            for i in range(len(cm)):
                cm[i] = list(cm[i])
            # Checking The Classes Names
            val = classes_check(classes_names, [*range(len(cm))], 2)
        # Creating The Confusion Matrix Heatmap (Png Format) In Working Direcory
        if detail:
            imshow_config(cm, val, True)
        else:
            imshow_config(cm, val, True, False)
        if len(cm) == 0:
            # Print Msg
            print("No HTML File Generated :(")
        elif len(cm) == 1:
            # Preparing Confusion Matrix
            data1 = [
                [
                    "",
                    f"Positive If Positive OR Negative If Negative ({val[0]})",
                ],
                [
                    f"Positive OR Negative ({val[0]})",
                    f"True Positive OR True Negative \n\n           TP OR TN : \n\n              {cm[0][0]}" if detail else cm[
                        0][0],
                ],
            ]
            # Preparing The Rate/Score Table
            data2 = [
                [
                    "",
                    "Rate (Score)",
                ],
                [
                    "Accuracy",
                    "1",
                ],
                [
                    "Error",
                    "0",
                ],
            ]
            # Preparing Classification Report
            data3 = [
                [
                    "Precision (P)",
                    "Recall (R)",
                    "F1-Score (F)",
                    "Support (S)",
                ],
                [
                    f"Positive OR Negative ({val[0]})",
                    "1",
                    "1",
                    "1",
                    f"{cm[0][0]}",
                ],
                [
                    "Macro Avg",
                    "1",
                    "1",
                    "1",
                    f"{cm[0][0]}",
                ],
                [
                    "Weighted Avg",
                    "1",
                    "1",
                    "1",
                    f"{cm[0][0]}",
                ],
            ]
            # Writing All Data
            with open("conf_mat.html", "w") as file:
                file.write("<u><b>Confusion Matrix</b></u> :\n<br>\n<br>\n")
                file.write(tabulate(data1, headers="firstrow",
                                    tablefmt="html") + "\n<br>\n<br>\n")
                file.write(tabulate(data2, headers="firstrow",
                                    tablefmt="html") + "\n<br>\n<br>\n")
                file.write(
                    "<u><b>Classification Report</b></u> :\n<br>\n<br>\n")
                file.write(
                    tabulate(data3, headers="firstrow", tablefmt="html") + "\n<br>\n<br>\n")
                file.write(
                    "<u><b>Confusion Matrix Display</b></u> : \n<br>\n<br>\n")
                file.write('<img src="conf_mat.png" alt="Confusion Matrix">\n')
            # Update HTML Code
            update_html()
            # Print The Success Msg
            print("\nHTML File Generated Successfully :)\n")
            # Opening HTML Page
            wb("conf_mat.html")
        elif len(cm) == 2:
            accuracy, error, precision, negative_precision, recall, specificity, support_1, support_0, f_score_1, f_score_0 = classification_report_calculation(
                cm)
            # Preparing Confusion Matrix
            data1 = [
                [
                    "Classes",
                    "Predicted Positive (PP)",
                    "Predicted Negative (PN)",
                    "",
                ],
                [
                    "Actual Positive (P)",
                    f"True Positive (TP) : {cm[1][1]}" if detail else cm[1][1],
                    f"False Negative (FN) / Type II Error (Missed) : {cm[1][0]}" if detail else cm[1][0],
                ],
                [
                    "Actual Negative (N)",
                    f"False Positive (FP) Type I Error (Wrong) : {cm[0][1]}" if detail else cm[0][1],
                    f"True Negative (TN) : {cm[0][0]}" if detail else cm[0][0],
                ],
            ]
            # Preparing The Rate/Score Table
            data2 = [
                [
                    "",
                    "Rate (Score)",
                ],
                [
                    "Accuracy",
                    f"Correct / Total : (TP + TN) / (TP + FP + FN + TN) = {round(accuracy, 2)}" if detail else round(
                        accuracy, 2),
                ],
                [
                    "Error",
                    f"Wrong / Total : (FP + FN) / (TP + FP + FN + TN) = {error}" if detail else error,
                ],
            ]
            # Preparing Classification Report
            data3 = [
                [
                    "Precision (P)",
                    "Recall (R)",
                    "F1-Score (F)",
                    "Support (S)",
                ],
                [
                    f"Positive ({val[1]})",
                    f"P1 (PPV): TP / (TP + FP) = {round(precision, 2)}" if detail else round(
                        precision, 2),
                    f"R1 (Sensitivity): TP / (TP + FN) = {round(recall, 2)}" if detail else round(
                        recall, 2),
                    f"F1 : (2 x P1 x R1) / (P1 + R1) = {round(f_score_1, 2)}" if detail else round(
                        f_score_1, 2),
                    f"S1 : TP + FN = {support_1}" if detail else support_1,
                ],
                [
                    f"Negative ({val[0]})",
                    f"P0 (NPV): TN / (TN + FN) = {round(negative_precision, 2)}" if detail else round(
                        negative_precision, 2),
                    f"R0 (Specificity): TN / (TN + FP) = {round(specificity, 2)}" if detail else round(
                        specificity, 2),
                    f"F0 : (2 x P0 x R0) /  (P0 + R0) = {round(f_score_0, 2)}" if detail else round(
                        f_score_0, 2),
                    f"S0 : FP + TN = {support_0}" if detail else support_0,
                ],
                [
                    "Macro Avg",
                    f"(P1 + P0) / 2 = {round((precision + negative_precision)/2, 2)}" if detail else round(
                        (precision + negative_precision)/2, 2),
                    f"(R1 + R0) / 2 = {round((recall + specificity)/2, 2)}" if detail else round(
                        (recall + specificity)/2, 2),
                    f"(F1 + F0) / 2 = {round((f_score_1 + f_score_0)/2, 2)}" if detail else round(
                        (f_score_1 + f_score_0)/2, 2),
                    f"TS = {support_0 + support_1}" if detail else support_0 + support_1,
                ],
                [
                    "Weighted Avg",
                    f"W1 / TS = {round(((precision * support_1) + (negative_precision * support_0))/(support_0 + support_1), 2)}" if detail else round(
                        ((precision * support_1) + (negative_precision * support_0))/(support_0 + support_1), 2),
                    f"W2 / TS = {round(((recall * support_1) + (specificity * support_0))/(support_0 + support_1), 2)}" if detail else round(
                        ((recall * support_1) + (specificity * support_0))/(support_0 + support_1), 2),
                    f"W3 / TS = {round(((f_score_1 * support_1) + (f_score_0 * support_0))/(support_1 + support_0),2)}" if detail else round(
                        ((f_score_1 * support_1) + (f_score_0 * support_0))/(support_1 + support_0), 2),
                    f"TS = {support_0 + support_1}" if detail else support_0 + support_1,
                ],
            ]
            # Writing All Data
            with open("conf_mat.html", "w") as file:
                file.write("<u><b>Confusion Matrix</b></u> : \n<br>\n<br>\n")
                file.write(tabulate(data1, headers="firstrow",
                           tablefmt="html") + "\n<br>\n<br>\n")
                file.write(tabulate(data2, headers="firstrow",
                           tablefmt="html") + "\n<br>\n<br>\n")
                file.write(
                    "<u><b>Classification Report</b></u> : \n<br>\n<br>\n")
                file.write(tabulate(data3, headers="firstrow",
                           tablefmt="html") + "\n<br>\n<br>\n")
                if detail:
                    file.write(
                        "<u><b>PPV</b></u> : Positive Predictive Value\n<br>\n<br>\n")
                    file.write(
                        "<u><b>NPV</b></u> : Negative Predictive Value\n<br>\n<br>\n")
                    file.write(
                        "<b>W1</b> = (P1 x S1) + (P0 x S0)\n<br>\n<br>\n")
                    file.write(
                        "<b>W2</b> = (R1 x S1) + (R0 x S0)\n<br>\n<br>\n")
                    file.write(
                        "<b>W3</b> = (F1 x S1) + (F0 x S0)\n<br>\n<br>\n")
                    file.write(
                        "<b>TS</b> : Total Support = S1 + S0\n<br>\n<br>\n<br>\n")
                    file.write(
                        "<u><b>Note</b></u> : All Real Numbers Are Rounded With Two Digits After The Comma\n<br>\n<br>\n<br>\n<br>")
                file.write(
                    "<u><b>Confusion Matrix Display</b></u> : \n<br>\n<br>\n")
                file.write('<img src="conf_mat.png" alt="Confusion Matrix">\n')
            # Update HTML Code
            update_html()
            # Print The Success Msg
            print("\nHTML File Generated Successfully :)\n")
            # Opening HTML Page
            wb("conf_mat.html")
        else:
            accuracy, error, class_repo, class_repo_con = classification_report_calculation(
                cm, val, True)
            # Concat The Classes with Confusion Matrix
            data1 = [val] + cm
            # Preparing The Rate/Score Table
            data2 = [
                [
                    "",
                    "Rate (Score)",
                ],
                [
                    "Accuracy",
                    f"Correct / Total : Sum Of Left Diagonal Values / Total (Sum Of All Matrix) OR  1 - Error = {round(accuracy, 2)}" if detail else round(
                        accuracy, 2),
                ],
                [
                    "Error",
                    f"Wrong / Total : (Total (Sum Of All Matrix) - Sum Of Left Diagonal Values) / Total (Sum Of All Matrix) OR  1 - Accuracy = {round(error, 2)}" if detail else round(
                        error, 2),
                ],
            ]
            # Concat The header Row With The Classification Report Matrix
            data3 = [["", "Precision (P)", "Recall (R)",
                     "F1-Score (F)", "Support (S)"]] + class_repo + class_repo_con
            # Writing All Data
            with open("conf_mat.html", "w") as file:
                file.write("<u><b>Confusion Matrix</b></u> : \n<br>\n<br>\n")
                file.write(tabulate(data1, headers="firstrow",
                           tablefmt="html") + "\n<br>\n<br>\n")
                file.write(tabulate(data2, headers="firstrow",
                           tablefmt="html") + "\n<br>\n<br>\n")
                file.write(
                    "<u><b>Classification Report<b></u> :\n<br>\n<br>\n")
                file.write(tabulate(data3, headers="firstrow",
                           tablefmt="html") + "\n<br>\n<br>\n")
                if detail:
                    file.write(
                        "<b><u>Precision</u></b> " + "&nbsp;" * 3 + ": Sum Of True Prediction For Each Value (Left Diagonal) / Sum Of Value Column\n<br>\n<br>\n")
                    file.write(
                        "<u><b>Recall</b></u>    " + "&nbsp;" * 8 + ": Sum Of True Prediction For Each Value (diagonal) / Sum Of Value Row\n<br>\n<br>\n")
                    file.write(
                        "<u><b>F1-Score</b></u>  " + "&nbsp;" * 3 + ": (2 x Precision x Recall) / (Precision + Recall)\n<br>\n<br>\n")
                    file.write(
                        "<u><b>Support</b></u>   " + "&nbsp;" * 5 + ": Sum Of Each Row\n<br>\n<br>\n")
                    file.write("<u><b>Macro Avg</b></u> :\n<br>\n<br>\n")
                    file.write(
                        "&nbsp;" * 15 + "Precision : (Sum Of Precision Column) / Classes Count\n<br>\n<br>\n")
                    file.write(
                        "&nbsp;" * 15 + "Recall    " + "&nbsp;" * 5 + ": (Sum Of Recall Column) / Classes Count\n<br>\n<br>\n")
                    file.write(
                        "&nbsp;" * 15 + "F1-Score  : (Sum Of F1-Score Column) / Classes Count\n<br>\n<br>\n")
                    file.write(
                        "&nbsp;" * 15 + "Support   " + "&nbsp;" * 2 + ": Total (Sum Of All Matrix)\n<br>\n<br>\n")
                    file.write("<u><b>Weighted Avg</b></u> :\n<br>\n<br>\n")
                    file.write(
                        "&nbsp;" * 15 + "Precision : (Sum Of (Precision x support)) / Total (Sum Of All Matrix)\n<br>\n<br>\n")
                    file.write(
                        "&nbsp;" * 15 + "Recall    " + "&nbsp;" * 5 + ": (Sum Of (Recall x Support)) / Total (Sum Of All Matrix)\n<br>\n<br>\n")
                    file.write(
                        "&nbsp;" * 15 + "F1-Score  : (Sum Of (F1-Score x Support)) / Total (Sum Of All Matrix)\n<br>\n<br>\n")
                    file.write(
                        "&nbsp;" * 15 + "Support   " + "&nbsp;" * 2 + ": Total (Sum Of All Matrix)\n<br>\n<br>\n<br>\n")
                    file.write(
                        "<u><b>Note</b></u> : All Real Numbers Are Rounded With Two Digits After The Comma\n<br>\n<br>\n<br>\n<br>\n")
                file.write(
                    "<u><b>Confusion Matrix Display</b></u> : \n<br>\n<br>\n")
                file.write('<img src="conf_mat.png" alt="Confusion Matrix">\n')
            # Update HTML Code
            update_html()
            # Print The Success Msg
            print("\nHTML File Generated Successfully :)\n")
            # Opening HTML Page
            wb("conf_mat.html")


def main(void: None) -> None:
    print("Hello, Work!")


if __name__ == "__main__":
    main(None)
