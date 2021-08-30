#! /usr/bin/env python
# -*- coding: utf-8 -*-

import c4d


def GetNextObject(op):
    if op is None:
        return None

    if op.GetDown():
        return op.GetDown()

    while not op.GetNext() and op.GetUp():
        op = op.GetUp()

    return op.GetNext()


def main():
    act_obj = c4d.documents.GetActiveDocument().GetActiveObject()
    fst_obj = c4d.documents.GetActiveDocument().GetFirstObject()

    if act_obj == fst_obj: return

    cur_obj = fst_obj

    while True:
        nxt = GetNextObject(cur_obj)
        if nxt == act_obj:
            nxt.DelBit(c4d.BIT_ACTIVE)
            cur_obj.SetBit(c4d.BIT_ACTIVE)
            c4d.EventAdd()
            break
        cur_obj = nxt


if __name__ == '__main__':
    main()
