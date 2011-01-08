from couchdbkit import Server, Database
from couchdbkit.loaders import FileSystemDocsLoader
import ROOT
import sys

if __name__=='__main__':

    uri = sys.argv[1]
    dbname = sys.argv[2]

    print 'Analyze contents of %s/%s' % (uri, dbname)

    # #connect to the db
    cloudant = Server(uri)
    db = cloudant.get_or_create_db(dbname)
    print db.info()

    #let's plot the number of accidents and fatalities vs time
    nt = ROOT.TNtuple('nt','Aviation Accident Ntuple','year:month:accidents:fatalities')

    
    for row in db.view('example/date',group=True,stale='ok'):
        year = row['key'][0]
        month = row['key'][1]
        accidents = row['value'][0]
        fatalities = row['value'][1]
        nt.Fill(year,month,accidents,fatalities)
        #
        
    #and plot
    c = ROOT.TCanvas('c')
    c.SetFillColor(0)
    ROOT.gStyle.SetOptStat(0)
    
    nt.SetMarkerStyle(20)
    nt.SetMarkerColor(1)
    nt.SetLineColor(1)
    nt.Draw('year>>+hacc(29,1981.5, 2010.5)','accidents','lp')
    hacc = ROOT.gROOT.Get('hacc')
    
    nt.SetMarkerStyle(24)
    nt.SetMarkerColor(2)
    nt.SetLineColor(2)
    nt.Draw('year>>+hfat(29,1981.5,2010.5)','fatalities','lpsame')
    hfat = ROOT.gROOT.Get('hfat')
    
    hacc.SetTitle('FAA Data by Year')
    hacc.SetXTitle('Year')
    
    #now find the year with the most accidents and inspect those 5 individually.  This is a job for search
    
    leg = ROOT.TLegend(0.5,0.65, 0.85, 0.8)
    leg.SetFillColor(0)
    leg.AddEntry(hacc,'Accidents','lp')
    leg.AddEntry(hfat,'Fatalities','lp')
    leg.Draw('same')
    
    
    c.SaveAs('accidents.png')

