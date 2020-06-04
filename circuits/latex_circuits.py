#!/usr/bin/env python

# TODO
# hashbang
# rename
# viz: generic 1 and 2 qubit gates
# Generic multiqubit gates?

from sympy import Symbol

import quantumflow as qf


def write_latex(fname, circ):
    scale = 0.75
    latex = qf.circuit_to_latex(circ, document=False, package='quantikz',
                                qubit_labels=False)
    with open(fname + '.tex', "w") as fout:
        fout.write(latex)

    print('.', end='')

fname = 'cnot'
circ = qf.Circuit([qf.CNOT(0, 1)])
write_latex(fname, circ)

fname = 'cnot_switch'
circ = qf.Circuit([qf.H(0), qf.H(1), qf.CNOT(1, 0), qf.H(0), qf.H(1)])
# assert equaltiy
write_latex(fname, circ)

fname = 'swap'
circ = qf.Circuit([qf.SWAP(0, 1)])
write_latex(fname, circ)

fname = 'swap_to_cnot'
circ = qf.Circuit([qf.CNOT(0, 1), qf.CNOT(1, 0), qf.CNOT(0, 1)])
write_latex(fname, circ)

fname = 'dcnot'
circ = qf.Circuit([qf.CNOT(0, 1), qf.CNOT(1, 0)])
write_latex(fname, circ)

fname = 'iswap_to_dcnot'
circ = qf.Circuit([qf.H(0), qf.S_H(0), qf.S_H(1), qf.ISWAP(1, 0), qf.H(1)])
write_latex(fname, circ)

# FIXME
# fname = 'magic'
# circ = qf.Circuit([qf.Unitary(name='M', qubits=[0, 1], tensor=qf.I(0, 1).tensor)])
# write_latex(fname, circ)

fname = 'magic_circ'
circ = qf.Circuit([qf.S(0), qf.S(1), qf.H(1), qf.CNOT(1, 0)])
write_latex(fname, circ)

# fname = 'qft'
# circ = qf.Circuit([qf.Unitary(qf.IDEN(0, 1).tensor, 0, 1, name='QFT')])
# write_latex(fname, circ)

fname = 'qft_circ'
circ = qf.Circuit([qf.SWAP(0, 1), qf.H(1), qf.CZ(0, 1), qf.H(0)])
write_latex(fname, circ)

fname = 'cz'
circ = qf.Circuit([qf.CZ(0, 1)])
write_latex(fname, circ)

fname = 'cv'
circ = qf.Circuit([qf.CV(0, 1)])
write_latex(fname, circ)

fname = 'cv_to_cpt'
circ = qf.Circuit(qf.translate_cv_to_cpt(qf.CV(0, 1)))
write_latex(fname, circ)

fname = 'cv2'
circ = qf.Circuit([qf.CV(0, 1), qf.CV(0, 1)])
write_latex(fname, circ)

fname = 'cnot_to_cz'
circ = qf.Circuit([qf.H(1), qf.CNOT(0, 1), qf.H(1)])
write_latex(fname, circ)

fname = 'ccnot'
circ = qf.Circuit([qf.CCNOT(0, 1, 2)])
write_latex(fname, circ)

fname = 'cswap'
circ = qf.Circuit([qf.CSWAP(0, 1, 2)])
write_latex(fname, circ)

fname = 'I'
circ = qf.Circuit([qf.I(0)])
write_latex(fname, circ)

fname = 'X'
circ = qf.Circuit([qf.X(0)])
write_latex(fname, circ)

fname = 'Y'
circ = qf.Circuit([qf.Y(0)])
write_latex(fname, circ)

fname = 'Z'
circ = qf.Circuit([qf.Z(0)])
write_latex(fname, circ)

fname = 'S'
circ = qf.Circuit([qf.S(0)])
write_latex(fname, circ)

fname = 'T'
circ = qf.Circuit([qf.T(0)])
write_latex(fname, circ)

fname = 'H'
circ = qf.Circuit([qf.H(0)])
write_latex(fname, circ)

fname = 'xx'
circ = qf.Circuit([qf.XX(Symbol('t'), 0, 1, )])
write_latex(fname, circ)

fname = 'yy'
circ = qf.Circuit([qf.YY(Symbol('t'), 0, 1, )])
write_latex(fname, circ)

fname = 'zz'
circ = qf.Circuit([qf.ZZ(Symbol('t'), 0, 1, )])
write_latex(fname, circ)

fname = 'RX'
circ = qf.Circuit([qf.RX(Symbol(r'\theta'))])
write_latex(fname, circ)

fname = 'RY'
circ = qf.Circuit([qf.RY(Symbol(r'\theta'))])
write_latex(fname, circ)

fname = 'RZ'
circ = qf.Circuit([qf.RZ(Symbol(r'\theta'))])
write_latex(fname, circ)

fname = 'TX'
circ = qf.Circuit([qf.TX(Symbol('t'))])
write_latex(fname, circ)

fname = 'TY'
circ = qf.Circuit([qf.TY(Symbol('t'))])
write_latex(fname, circ)

fname = 'TZ'
circ = qf.Circuit([qf.TZ(Symbol('t'))])
write_latex(fname, circ)

# FIXME
# fname = 'ph'
# circ = qf.Circuit([qf.Unitary(name='h', qubits=[0], tensor=qf.I(0).tensor)])
# write_latex(fname, circ)

# FIXME
# fname = 'inv_ph'
# circ = qf.Circuit([qf.Unitary(name=Symbol(r'h$^\dagger$'),
#                            qubits=[0], tensor=qf.I(0).tensor)])
# write_latex(fname, circ)

fname = 'ecp'
circ = qf.Circuit([qf.ECP()])
write_latex(fname, circ)

fname = 'ecp_to_sqrtiswap'
circ = qf.Circuit(qf.translate_ecp_to_sqrtiswap(qf.ECP()))
write_latex(fname, circ)

fname = 'w_to_ecp'
circ = qf.Circuit(qf.translate_w_to_ecp(qf.W()))
write_latex(fname, circ)

fname = 'w_to_ch_cnot'
circ = qf.Circuit(qf.translate_w_to_ch_cnot(qf.W()))
write_latex(fname, circ)

fname = 'w_to_cnot'
circ = qf.Circuit(qf.translate_w_to_cnot(qf.W()))
write_latex(fname, circ)


fname = 'peres'
circ = qf.Circuit(qf.CCNOT(0, 1, 2), qf.CNOT(0, 1))
write_latex(fname, circ)

deutsch = qf.Deutsch(Symbol(r'\theta'), 0, 1, 2)
fname = 'deutsch'
circ = qf.Circuit(deutsch)
write_latex(fname, circ)

fname = 'deutsch_to_barenco'
circ = qf.Circuit(qf.translate_deutsch_to_barenco(deutsch))
write_latex(fname, circ)

print()
