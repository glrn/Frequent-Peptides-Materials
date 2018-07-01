import os

proteins = {}
proteins["AAAAAAAAAA"] = 86
proteins["EEEEEEEEEE"] = 85
proteins["QQQQQQQQQQ"] = 65
proteins["PPPPPPPPPP"] = 62
proteins["SSSSSSSSSS"] = 55
proteins["GGGGGGGGGG"] = 50
proteins["DEEEEEEEEE"] = 34
proteins["EEEEEEEEED"] = 34
proteins["SAAAAAAAAA"] = 32
proteins["AAAAAAAAAG"] = 30
proteins["PPPPPPPPPL"] = 28
proteins["PPPPPPPPLP"] = 28
proteins["EEEEEEEEDE"] = 26
proteins["AAAAAAAAAS"] = 25
proteins["EEEEEEEEEG"] = 25
proteins["LPPPPPPPPP"] = 24
proteins["PPPPPPLPPP"] = 23
proteins["EEEDEEEEEE"] = 23
proteins["PPPPPPPLPP"] = 22
proteins["EDEEEEEEEE"] = 22
proteins["EEEEDEEEEE"] = 22
proteins["EEDEEEEEEE"] = 22
proteins["PPPPPPPPPA"] = 21
proteins["EEEEEEEDEE"] = 21
proteins["EEEEEEDEEE"] = 20
proteins["SGGGGGGGGG"] = 20
proteins["APPPPPPPPP"] = 20
proteins["ASSSSSSSSS"] = 20
proteins["HHHHHHHHHH"] = 20
proteins["QQQQQQQQQP"] = 18
proteins["AAAAAAAAAV"] = 18
proteins["EEEEEDEEEE"] = 18
proteins["QVKIWFQNRR"] = 18
proteins["EEEEEEEEEA"] = 17
proteins["HQRIHTGEKP"] = 17
proteins["IHTGEKPYKC"] = 16
proteins["GGGGGGGGGS"] = 16
proteins["CQGDSGGPLV"] = 16
proteins["QPPPPPPPPP"] = 16
proteins["GGGGGGGSGG"] = 16

def colorize(prob):
    if prob == '$> 10^{-3}$':
        return prob
    e = int(prob[prob.find('E')+1:])
    if e in [0, -1, -2, -3]:
        lvl = 0
    elif e in [-4, -5]:
        lvl = 1
    elif e in [-6, -7]:
        lvl = 2
    elif e in [-8, -9]:
        lvl = 3
    else:
        lvl = 4
    
    return '\cellcolor{lvl%d}%s' % (lvl, prob)

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def get_p_q_values_of_html(html):
    # print 4th and 5th "<td align="center">"
    str = '<td align="center">'
    p_value =  html[find_nth(html, str, 4)+len(str):html.find('</td',find_nth(html, str, 4)+len(str))]
    q_value = html[find_nth(html, str, 5)+len(str):html.find('</td',find_nth(html, str, 5)+len(str))]
    return p_value, q_value

for f in os.listdir('.'):

    peptide = f[3:]

    if os.path.isdir(f):
        process_path = f+'/process/Results.html'
        function_path = f+'/function/Results.html'
        component_path = f+'/component/Results.html'
        
        try:
            process_html = ''.join(open(process_path,'r').readlines())
            #print 'Best p/q values for Process:'
            process_p_value, process_q_value = get_p_q_values_of_html(process_html)
        except:
            process_p_value = '$> 10^{-3}$'
            process_q_value = '$> 10^{-3}$'
            
        try:
            function_html = ''.join(open(function_path,'r').readlines())
            #print 'Best p/q values for Function:'
            function_p_value, function_q_value = get_p_q_values_of_html(function_html)
        except:
            function_p_value = '$> 10^{-3}$'
            function_q_value = '$> 10^{-3}$'
            
        try:
            component_html = ''.join(open(component_path,'r').readlines())
            #print 'Best p/q values for Component:'
            component_p_value, component_q_value = get_p_q_values_of_html(component_html)
        except:
            component_p_value = '$> 10^{-3}$'
            component_q_value = '$> 10^{-3}$'
            
        print '\kmer{%s}&	%d& %s&   %s&    %s&   %s&    %s&   %s \\\\' % \
                (peptide, proteins[peptide],
                    colorize(process_p_value), colorize(process_q_value),
                    colorize(function_p_value), colorize(function_q_value),
                    colorize(component_p_value), colorize(component_q_value))