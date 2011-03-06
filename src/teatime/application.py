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
        self.slider_update = wx.Timer(self)

    def CreateMainPanel(self):
        # TODO: do we need a panel here or is a sizer enough?
        panel = wx.Panel(self, -1)
        sizer = wx.FlexGridSizer(rows=1, cols=2, hgap=5)
        label = wx.StaticText(panel, -1, "Time")
        sizer.Add(label, 0, 0)
        self.slider = wx.Slider(panel, -1, self.time_val, 0, 600,
                                size=(200,-1), style=wx.SL_HORIZONTAL |
                                wx.SL_AUTOTICKS | wx.SL_LABELS)
        sizer.Add(self.slider, 1, 0)
        self.slider.SetTickFreq(30, 1)
        self.slider.SetPageSize(30)
        self.slider.Bind(wx.EVT_SCROLL_CHANGED, self.OnSlide)
        panel.SetSizer(sizer)
        return panel

    def OnSlide(self, event):
        self.time_val = event.GetPosition()
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.timer.Start(self.time_val * 1000, oneShot=True)
        self.Bind(wx.EVT_TIMER, self.OnSliderUpdate, self.slider_update)
        self.slider_update.Start(1000)

    def OnTimer(self, event):
        self.slider_update.Stop()
        dlg = wx.MessageDialog(self,
                               "Mind the tea!", "Tea!?",
                               style=wx.OK, pos=wx.DefaultPosition)
        dlg.Raise()
        dlg.Iconize(False)
        dlg.ShowModal()
        dlg.Destroy()

    def OnSliderUpdate(self, event):
        self.time_val -= 1
        self.slider.SetValue(self.time_val)
    
def main():
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()
    return 0

if __name__ == '__main__':
    sys.exit(main())
