from gnuradio import gr

chan1 = 2412e6
chan13 = 2472e6

step = 15e6

curr_chan = chan1

def sweep(prob_lvl):
    global chan1,chan13,step,curr_chan

    if prob_lvl:
        curr_chan += step

    if curr_chan >= chan13:
        curr_chan = chan1

    return curr_chan
