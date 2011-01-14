from couchdbkit import Server, Database
from couchdbkit.loaders import FileSystemDocsLoader
import sys
from ROOT import *

if __name__=='__main__':
    uri = sys.argv[1]
    dbname = sys.argv[2]

    print 'Analzye contents of %s/%s' % (uri, dbname)

    # #connect to the db
    cloudant = Server(uri)
    db = cloudant[dbname]
    print db.info()

    nt = TNtuple('nt','FAA Data','year:month:accidents:fatalities')

    for row in db.view('example/date',group=True):
        year = row['key'][0]
        month = row['key'][1]
        accidents = row['value'][0]
        fatalities = row['value'][1]
        nt.Fill(year, month, accidents, fatalities)
    #
    c = TCanvas('c')
    c.SetFillColor(0)
    gStyle.SetOptStat(0)
    gPad.SetGrid(1,1)
    
    nt.SetMarkerStyle(20)
    nt.SetLineColor(1)
    nt.SetMarkerColor(1)
    nt.Draw('year>>+acc(23,1987.5, 2010.5)','accidents','lp')
    nt.SetMarkerStyle(24)
    nt.SetLineColor(2)
    nt.SetMarkerColor(2)
    nt.Draw('year>>+fat(23,1987.5,2010.5)','fatalities','lpsame')
    
    #weird root object access
    acc = gROOT.Get('acc')
    fat = gROOT.Get('fat')
    # print acc, fat
    acc.SetTitle('FAA Data vs Year from %s' % uri)
    acc.SetXTitle('year')
    acc.DrawCopy('lp')
    fat.DrawCopy('lpsame')
    
    leg = TLegend(0.6, 0.7, 0.85, 0.85)
    leg.SetFillColor(0)
    leg.AddEntry(acc,'Accidents','lp')
    leg.AddEntry(fat,'Fatalities','lp')
    leg.Draw('same')
    
    

    c.SaveAs('faa.png')