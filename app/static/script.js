(function(d3) {
    'use strict'

    var dataset = [
        { label: 'Male', count: 1000 },
        { label: 'Female', count: 100 }
    ];

    var width = 360;
    var height = 360;
    var radius = Math.min(width, height) / 2;

    // Defines color scale - if more than 20 entries in dataset, colors will be reused
    // var color = d3.scaleOrdinal(d3.schemeCategory20b);

    var color = d3.scaleOrdinal()
        .range(['blue', 'pink']);

    // Define svg
    var svg = d3.select('#chart')
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .append('g')
        .attr('transform', 'translate(' + (width / 2) +  ',' + (height / 2) + ')');

    var arc = d3.arc()
        .innerRadius(0)
        .outerRadius(radius);

    var pie = d3.pie()
        .value(function(d) {
            return d.count;
        })
        .sort(null);

    var path = svg.selectAll('path')
            .data(pie(dataset))
            .enter()
            .append('path')
            .attr('d', arc)
            .attr('fill', function(d, i) {
                return color(d.data.label);
            });

    // var csv = 'static/artist-gender-data.csv';

    // d3.csv(csv, function(error, dataset) {
    //     if (error) {
    //         console.log(error);
    //     }
    //     dataset.forEach(function(d) {
    //         d.count = +d.count;
    //     });

    //     var path = svg.selectAll('path')
    //         .data(pie(dataset))
    //         .enter()
    //         .append('path')
    //         .attr('d', arc)
    //         .attr('fill', function(d, i) {
    //             return color(d.data.label);
    //         });
    // })

})(window.d3);
