#-*- coding: utf-8 -*-

# Copyright 2011 Bastian Bowe
#
# This file is part of TeaTime.
# Teatime is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# TeaTime is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with TeaTime.  If not, see
# <http://www.gnu.org/licenses/>.

import sys
import wx

class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "TeaTimer")
        sizer = wx.BoxSizer()
        self.time_val = 0
        panel = self.CreateMainPanel()
        sizer.Add(panel, 0, 0)
        self.SetSizer(sizer)
        self.Fit()
        self.timer = wx.Timer(self)

    def CreateMainPanel(self):
        # TODO: do we need a panel here or is a sizer enough?
        panel = wx.Panel(self, -1)
        sizer = wx.FlexGridSizer(rows=1, cols=2, hgap=5)
        label = wx.StaticText(panel, -1, "Time")
        sizer.Add(label, 0, 0)
        slider = wx.Slider(panel, -1, self.time_val, 0, 600, size=(200,-1),
                           style=wx.SL_HORIZONTAL |
                           wx.SL_AUTOTICKS | wx.SL_LABELS)
        sizer.Add(slider, 1, 0)
        slider.SetTickFreq(30, 1)
        slider.Bind(wx.EVT_SCROLL_CHANGED, self.OnSlide)
        panel.SetSizer(sizer)
        return panel

    def OnSlide(self, event):
        self.time_val = event.GetPosition()
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.timer.Start(self.time_val * 1000, oneShot=True)

    def OnTimer(self, event):
        dlg = wx.MessageDialog(self,
                               "Mind the tea! (after %ss)" % self.time_val,
                               "Tea!?", style=wx.OK, pos=wx.DefaultPosition)
        dlg.ShowModal()
        dlg.Destroy()
    
def main():
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()
    return 0

if __name__ == '__main__':
    sys.exit(main())
