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
    cur_obj = c4d.documents.GetActiveDocument().GetActiveObject()
    if nxt_obj := GetNextObject(cur_obj):
        cur_obj.DelBit(c4d.BIT_ACTIVE)
        nxt_obj.SetBit(c4d.BIT_ACTIVE)
        c4d.EventAdd()


if __name__ == '__main__':
    main()
