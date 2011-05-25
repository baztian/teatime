#-*- coding: utf-8 -*-

# Copyright 2011 Bastian Bowe
#
# This file is part of TeaTime.
# Teatime is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# TeaTime is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with TeaTime.  If not, see <http://www.gnu.org/licenses/>.

import sys
import wx

def time_str(seconds):
    text = [ "%d seconds" % seconds ]
    if seconds > 60:
        mins = seconds / 60
        rest = seconds - mins * 60
        text.append("(%d:%d minutes)" % (mins, rest))
    return " ".join(text)

class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "TeaTimer")
        sizer = wx.BoxSizer()
        self.time_val = 0
        self.scrolling = False
        sizer = self.CreateMainPanel(self)
        self.SetSizer(sizer)
        self.Fit()
        size = sizer.GetMinSize()
        self.SetMinSize(size)
        self.timer = wx.Timer(self)
        self.slider_update = wx.Timer(self)

    def CreateMainPanel(self, panel):
        sizer = wx.FlexGridSizer(rows=2, cols=1, hgap=5)
        sizer.AddGrowableCol(0)
        self.label = wx.StaticText(panel, -1, time_str(0))
        sizer.Add(self.label, flag=wx.EXPAND)
        self.slider = wx.Slider(panel, -1, self.time_val, 0, 600,
                                size=(200,-1), style=wx.SL_HORIZONTAL |
                                wx.SL_AUTOTICKS)
        sizer.Add(self.slider, flag=wx.EXPAND)
        self.slider.SetTickFreq(30, 1)
        self.slider.SetPageSize(30)
        self.slider.Bind(wx.EVT_SCROLL_CHANGED, self.OnScrollChanged)
        self.slider.Bind(wx.EVT_SCROLL, self.OnScroll)
        return sizer

    def OnScroll(self, event):
        self.scrolling = True
        seconds = event.GetPosition()
        self.label.SetLabel(time_str(seconds))
        event.Skip()

    def OnScrollChanged(self, event):
        self.scrolling = False
        self.time_val = event.GetPosition()
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.timer.Start(self.time_val * 1000, oneShot=True)
        self.Bind(wx.EVT_TIMER, self.OnSliderUpdate, self.slider_update)
        self.slider_update.Start(1000)

    def OnTimer(self, event):
        self.slider_update.Stop()
        self.slider.SetValue(0)
        self.label.SetLabel(time_str(0))
        self.scrolling = False
        dlg = wx.MessageDialog(self, "Mind the tea!", "Tea!?",
                               style=wx.OK, pos=wx.DefaultPosition)
        self.Iconize(False)
        dlg.Iconize(False)
        dlg.Raise()
        self.Raise()
        dlg.ShowModal()
        dlg.Destroy()

    def OnSliderUpdate(self, event):
        self.time_val -= 1
        if self.scrolling:
            return
        self.slider.SetValue(self.time_val)
        self.label.SetLabel(time_str(self.time_val))
    
def main():
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()
    return 0

if __name__ == '__main__':
    sys.exit(main())
