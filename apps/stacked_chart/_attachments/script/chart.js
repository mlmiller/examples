$(function() {
  var maxElements = 150;

  var renderChart = function(config) {
    var chart;
    var containerele = config.containerele;
    var renderTo = containerele + '-graph';
    var loadingEle = containerele + '-loading';
    var title = config.title || "Chart Title";
    var yAxisTitle = config.yAxisTitle || "Y Axis Title";
    var xAxisTitle = config.xAxisTitle || "X Axis Title";
    
    
    var barChartOptions = {
      chart: {
         renderTo: renderTo,
         defaultSeriesType: 'column',
         margin: [ 50, 50, 100, 80]
      },
      title: {
         text: title
      },
      subtitle: {
         text: 'Click the legend to toggle data on/off'
      },
      xAxis: {
         categories: [], // need to set this
         labels: {
            rotation: -45,
            align: 'right',
            style: {
                font: 'normal 11px Verdana, sans-serif'
            }
         }
      },
      yAxis: {
         min: 0,
         title: {
            text: yAxisTitle
         },
         stackLabels: {
            enabled: true,
            style: {
               fontWeight: 'bold',
               color: (Highcharts.theme && Highcharts.theme.textColor) || 'gray'
            }
         }
      },
      legend: {
         layout: 'vertical',
         align: 'right', 
         // x: -100,
         verticalAlign: 'top',
         y: 40,
         floating: true,
         backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColorSolid) || 'white',
         borderColor: '#CCC',
         borderWidth: 1,
         shadow: false
      },
      // legend: {
      //    enabled: false
      // },
      tooltip: {
          formatter: function() {
                      return '<b>'+ this.x +'</b><br/>'+
                          this.series.name +': '+ this.y +'<br/>'+
                          'Total: '+ this.point.stackTotal;                   }
      },
      plotOptions: {
         column: {
            stacking: 'normal',
            dataLabels: {
               enabled: true,
               color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white'
            }
         }
      },

       series: [],
   };
   
   //ok, here's where we assume a single view query per chart

    var db = $.couch.db(config.couchdatabase);
    db.view(config.couchdesign +'/'+ config.couchview, { "include_docs":"true","descending":"true", "success":function(response) {
      $('#'+loadingEle).remove();

      var data = config.rowsCallback(response.rows.slice(0,maxElements));
      
      //the config declares the actual data, its description, and dimensionality
      barChartOptions.series = config.series;
      barChartOptions.xAxis.categories = data[0];
      for (var iseries=1; iseries<barChartOptions.series.length+1; iseries++) {
          barChartOptions.series[iseries-1].data = data[iseries];
      }

      if (config.tooltipFormatter) {
        barChartOptions.tooltip.formatter = config.tooltipFormatter;
      }

      chart = new Highcharts.Chart(barChartOptions);
    }});

    var $container = $('#'+renderTo).css('position', 'relative');
    
  };

  //chart specific definitions
  var theDataLabels = {
      enabled: false,
      rotation: -90,
      color: Highcharts.theme.dataLabelsColor || '#FFFFFF',
      align: 'right',
      x: -3,
      y: 10,
      formatter: function() {
          return this.y;
      },
      style: {
          font: 'normal 9px Verdana, sans-serif'
      }
     };
  
  var configs = {
      
      //primary chart
      'primary' :{
        containerele : 'chart1',
        couchdatabase : 'esi_final', 
        couchdesign : 'stacked_chart',
        couchview : 'final',
        title : 'Doctor Rankings',
        yAxisTitle : 'Relative Activity Rank',
        series: [
           {
            name: 'Mean Procedures per Day Ranking',
            data: [], // need to set this
            dataLabels: theDataLabels,
            },
            {
             name: 'Total Procedure Ranking',
             data: [], // need to set this
             dataLabels: theDataLabels,
             },
             {
              name: 'Unique Insureds Billed Ranking',
              data: [], // need to set this
              dataLabels: theDataLabels,
              },
             {
              name: 'Mean Dollars Billed per Day Ranking',
              data: [], // need to set this
              dataLabels: theDataLabels,               
              },
          ],
        rowsCallback : function(rows) {
          var result = [
            [], // xAxis data points
            [],  // yAxis data points
            [], //yAxis data points
            [],  // yAxis data points
            [], //yAxis data points
          ];

          jQuery.each(rows, function(i, row) {
              // console.log( [row.key[0], row.value.sum]);
              var rank = row.doc.rank;
              result[0].push( row.value); // get the x-values
              result[1].push( Math.round((1.-rank.mean_procs)*1000)/ 1000); // Mean Procs / day worked
              result[2].push( Math.round((1.-rank.total_procs)*1000)/ 1000);
              result[3].push( Math.round((1.-rank.unique_insureds)*1000)/ 1000);
              result[4].push( Math.round((1.-rank.mean_billed)*1000)/ 1000);
          });        
          return result;
        },
        // Optional tooltip formatter function
        // Optional tooltip formatter function
        tooltipFormatter : function() {
            return '<b>'+ this.x +'</b><br/>'+
                this.series.name +': '+ this.y +'<br/>'+
                'Percentile Rank: '+ this.point.stackTotal;
        }
      },
      
      //secondary chart
      'secondary' :{
        containerele : 'chart1',
        couchdatabase : 'esi_final', 
        couchdesign : 'stacked_chart',
        couchview : 'final',
        title : 'Doctor Rankings',
        yAxisTitle : 'Summed count',
        series: [
           {
            name: 'Mean Procedures per Day',
            data: [], // need to set this
            dataLabels: theDataLabels,
            },
            {
             name: 'Total Procedures',
             data: [], // need to set this
             dataLabels: theDataLabels,
             },
             {
              name: 'Unique Insureds Billed',
              data: [], // need to set this
              dataLabels: theDataLabels,
              },
             {
              name: 'Mean Dollars Billed per Day',
              data: [], // need to set this
              dataLabels: theDataLabels,               
              },
          ],
        rowsCallback : function(rows) {
          var result = [
            [], // xAxis data points
            [],  // yAxis data points
            [], //yAxis data points
            [],  // yAxis data points
            [], //yAxis data points
          ];

          jQuery.each(rows, function(i, row) {
              // console.log( [row.key[0], row.value.sum]);
              var doc = row.doc;    
              result[0].push( row.value); // get the x-values
              result[1].push( doc.mean_procs);
              result[2].push( doc.total_procs );
              result[3].push( doc.unique_insureds);
              result[4].push( doc.mean_billed);
          });        
          return result;s
        },
        // Optional tooltip formatter function
        // Optional tooltip formatter function
        tooltipFormatter : function() {
            return '<b>'+ this.x +'</b><br/>'+
                this.series.name +': '+ this.y +'<br/>'+
                'Summed Values: '+ this.point.stackTotal;
        }
      }
      
  };

  $('ul.pills li a').click(function(event) {
          event.preventDefault();
          var pillID = $(this).parent().attr('id');
          renderChart(configs[pillID]);
          $('ul.pills li').removeClass('active');
          $(this).parent().addClass('active');
  });
  
  renderChart(configs['primary']);
});
