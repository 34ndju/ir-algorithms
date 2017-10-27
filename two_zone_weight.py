# g is t's weight, and (1-g) is b's weight
# 1 indicates a presence in t, b respectively (0 vice-versa)
# our derived two weight equaltion is (#10r + #01n)/(#10r + #10n + #01r + #01n)
def determine_g_weight(training_set):
    numerator = 0
    denominator = 0

    for train in training_set:
        if (train['t'] and not train['b'] and train['judgement']) or (not train['t'] and train['b'] and not train['judgement']):
            numerator += 1
            denominator +=1
        elif (train['t'] and not train['b'] and not train['judgement']) or (not train['t'] and train['b'] and train['judgement']):
            denominator += 1

    return numerator / float(denominator)

training_set = []
training_set.append({'t':True, 'b':True, 'judgement':True})
training_set.append({'t':False, 'b':True, 'judgement':False})
training_set.append({'t':False, 'b':True, 'judgement':True})
training_set.append({'t':False, 'b':False, 'judgement':False})
training_set.append({'t':True, 'b':True, 'judgement':True})
training_set.append({'t':False, 'b':True, 'judgement':True})
training_set.append({'t':True, 'b':False, 'judgement':False})

print determine_g_weight(training_set)
# 0.25
