var w = window.innerWidth;
var h = window.innerHeight;

var focus_node = null,
    highlight_node = null;

var text_center = true;
var outline = false;

var min_score = 0;
var max_score = 1;

var color = d3.scale.linear()
    .domain([min_score, (min_score + max_score) / 2, max_score])
    .range(["lime", "yellow", "red"]);

var highlight_color = "rgb(33,38,240)";
var highlight_trans = 0.1;

var size = d3.scale.pow().exponent(1)
    .domain([1, 100])
    .range([8, 24]);

var force = d3.layout.force()
    .linkDistance(60)
    .charge(-300)
    .size([w, h]);

//var default_node_color = "#ccc";
var default_link_color = "#888";
var nominal_base_node_size = 8;
var nominal_text_size = 10;
var max_text_size = 24;
var nominal_stroke = 0.5;
var max_stroke = 4.5;
var max_base_node_size = 36;
var min_zoom = 0.1;
var max_zoom = 7;

var techtree = d3.select("#techtree")
var svg = techtree.append("svg");
var readme = techtree.append("div").attr("id", "readme")

var zoom = d3.behavior.zoom().scaleExtent([min_zoom, max_zoom])
var g = svg.append("g");
svg.style("cursor", "move");

src = document.getElementById("techtree").getAttribute("src")
d3.json(src, function(error, graph) {

    var linkedByIndex = {};
    graph.links.forEach(function(d) {
        linkedByIndex[d.source + "," + d.target] = true;
    });

    function isConnected(a, b) {
        return linkedByIndex[a.index + "," + b.index] || linkedByIndex[b.index + "," + a.index] || a.index == b.index;
    }

    function hasConnections(a) {
        for (var property in linkedByIndex) {
            s = property.split(",");
            if ((s[0] == a.index || s[1] == a.index) && linkedByIndex[property]) return true;
        }
        return false;
    }

    force
        .nodes(graph.nodes)
        .links(graph.links)
        .start();

    var link = g.selectAll(".link")
        .data(graph.links)
        .enter().append("line")
        .attr("class", "link")
        .style("stroke-width", nominal_stroke)


    var node = g.selectAll(".node")
        .data(graph.nodes)
        .enter().append("g")
        .attr("class", "node")
        .call(force.drag);


    node.on("dblclick.zoom", function(d) {
        d3.event.stopPropagation();
        var dcx = (window.innerWidth / 2 - d.x * zoom.scale());
        var dcy = (window.innerHeight / 2 - d.y * zoom.scale());
        zoom.translate([dcx, dcy]);
        g.attr("transform", "translate(" + dcx + "," + dcy + ")scale(" + zoom.scale() + ")");
    });

    node.on("click", function(d){
        // TODO
        // show rendered readme.md
    });


    var tocolor = "fill";
    var towhite = "stroke";
    if (outline) {
        tocolor = "stroke"
        towhite = "fill"
    }

    var circle = node.append("path")
        .attr("d", d3.svg.symbol()
            .size(function(d) {
                return Math.PI * Math.pow(size(d.size) || nominal_base_node_size, 2);
            })
            .type(function(d) {
                return d.type;
            }))
        //.attr("r", function(d) { return size(d.size)||nominal_base_node_size; })
        .style("stroke-width", nominal_stroke)

    var text = node.append("text").attr("d", d3.svg.symbol())
            .style("font-size", nominal_text_size + "px")
            .text(function(d){ return d.id })
            .attr("dy", function(d){
             return ((d.size)*0.05 || nominal_base_node_size) * 0.25 + "em"
            })
            ;

    if (text_center)
        text.text(function(d) {
            return d.id;
        })
        .style("text-anchor", "middle");
    else
        text.attr("dx", function(d) {
            return (size(d.size) || nominal_base_node_size);
        })
        .text(function(d) {
            return '\u2002' + d.id;
        });

    node.on("mouseover", function(d) {
            set_highlight(d);
        })
        .on("mousedown", function(d) {
            d3.event.stopPropagation();
            focus_node = d;
            set_focus(d)
            if (highlight_node === null) set_highlight(d)

        }).on("mouseout", function(d) {
            exit_highlight();

        });



    d3.select(window).on("mouseup",
        function() {
            if (focus_node !== null) {
                focus_node = null;
                if (highlight_trans < 1) {

                    circle.style("opacity", 1);
                    text.style("opacity", 1);
                    link.style("opacity", 1);
                }
            }

            if (highlight_node === null) exit_highlight();
        });

    function exit_highlight() {
        highlight_node = null;
        if (focus_node === null) {
            svg.style("cursor", "move");
            if (highlight_color != "white") {
                node.attr('class', 'node');
                link.attr("class", "link");
            }

        }
    }

    function set_focus(d) {
        if (highlight_trans < 1) {
            circle.style("opacity", function(o) {
                return isConnected(d, o) ? 1 : highlight_trans;
            });

            text.style("opacity", function(o) {
                return isConnected(d, o) ? 1 : highlight_trans;
            });

            link.style("opacity", function(o) {
                return o.source.index == d.index || o.target.index == d.index ? 1 : highlight_trans;
            });
        }
    }


    function set_highlight(d) {
        svg.style("cursor", "pointer");
        if (focus_node !== null) d = focus_node;
        highlight_node = d;


        node.attr('class', function(o){
            return isConnected(d, o) ? 'node highlighted' : 'node'
        });

        if (highlight_color != "white") {
            link.attr("class", function(o) {
                return o.source.index == d.index || o.target.index == d.index ? "link highlighted" : "link"
            });
        }
    }


    zoom.on("zoom", function() {

        var stroke = nominal_stroke;
        if (nominal_stroke * zoom.scale() > max_stroke) stroke = max_stroke / zoom.scale();
        link.style("stroke-width", stroke);
        circle.style("stroke-width", stroke);

        var base_radius = nominal_base_node_size;
        if (nominal_base_node_size * zoom.scale() > max_base_node_size) base_radius = max_base_node_size / zoom.scale();
        circle.attr("d", d3.svg.symbol()
            .size(function(d) {
                return Math.PI * Math.pow(size(d.size) * base_radius / nominal_base_node_size || base_radius, 2);
            })
            .type(function(d) {
                return d.type;
            }))

        //circle.attr("r", function(d) { return (size(d.size)*base_radius/nominal_base_node_size||base_radius); })
        if (!text_center) text.attr("dx", function(d) {
            return (size(d.size) * base_radius / nominal_base_node_size || base_radius);
        });

        var text_size = nominal_text_size;
        if (nominal_text_size * zoom.scale() > max_text_size) text_size = max_text_size / zoom.scale();
        text.style("font-size", text_size + "px");

        g.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
    });

    svg.call(zoom);

    resize();
    //window.focus();
    d3.select(window).on("resize", resize)

    force.on("tick", function() {

        node.attr("transform", function(d) {
            return "translate(" + d.x + "," + d.y + ")";
        });

        link.attr("x1", function(d) {
                return d.source.x;
            })
            .attr("y1", function(d) {
                return d.source.y;
            })
            .attr("x2", function(d) {
                return d.target.x;
            })
            .attr("y2", function(d) {
                return d.target.y;
            });

        node.attr("cx", function(d) {
                return d.x;
            })
            .attr("cy", function(d) {
                return d.y;
            });
    });

    function resize() {
        var width = window.innerWidth,
            height = window.innerHeight;
        svg.attr("width", width).attr("height", height);

        force.size([force.size()[0] + (width - w) / zoom.scale(), force.size()[1] + (height - h) / zoom.scale()]).resume();
        w = width;
        h = height;
    }


});

function vis_by_type(type) {
    return true
}

function vis_by_node_score(score) {
    if (isNumber(score)) {
        if (score >= 0.666) return keyh;
        else if (score >= 0.333) return keym;
        else if (score >= 0) return keyl;
    }
    return true;
}

function vis_by_link_score(score) {
    if (isNumber(score)) {
        if (score >= 0.666) return key3;
        else if (score >= 0.333) return key2;
        else if (score >= 0) return key1;
    }
    return true;
}

function isNumber(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
}

