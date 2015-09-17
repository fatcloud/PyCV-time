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
var highlight_trans = 0.3;

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
var readme = techtree.append("div").attr("id", "readme");

var zoom = d3.behavior.zoom().scaleExtent([min_zoom, max_zoom])

var github_api_raw_path = "https://raw.githubusercontent.com/fatcloud/PyCV-time/";
var github_api_content_path = "https://api.github.com/repos/fatcloud/PyCV-time/contents/";

var not_found_content = "";
var information_content = "";
$.ajax({
    url: github_api_content_path + 'readme/techtree.md?ref=gh-pages',
    headers: {
        "Accept": 'application/vnd.github.v3.html; application/json'
    },
    success: function(results) {
        information_content = results;
        show_info(information_content);
    }
});
$.ajax({
    url: github_api_content_path + 'readme/not-found.md?ref=gh-pages',
    // https://api.github.com/repos/fatcloud/PyCV-time/contents/readme?ref=gh-pages
    headers: {
        "Accept": 'application/vnd.github.v3.html; application/json'
    },
    success: function(results) {
        // var reg = new RegExp("(href|src)=\"(?!http|#)([^\"]+)\"","gi");
        // results = results.replace(reg, function(t){
        //     var sps = t.split('"');
        //     sps[1] = raw_content_base + "/" + sps[1]; 
        //     return sps.join('"');
        // });
        not_found_content = results;
    }
});

var gen_show_info = function(elementId){
    var el = $(document.getElementById(elementId));
    if(!el.hasClass('readme-parsed')){
        var childString = '<div class="readme-opts"></div><div class="readme-body"></div>'+
            '<div class="readme-toggle"><div class="readme-toggle-offset"><span class="readme-toggle-text">\u25b6</span></div></div>';
        el.append(childString);
        el.addClass('readme-parsed');

        $(document.body).append('<div class="readme-alert-main"><div class="readme-alert-body"></div></div>');
        var target = el.find(".readme-toggle-offset");
        el.find(".readme-toggle-offset").click(function(e){
            if($(this).hasClass("open")){
                hide_info();
            }else{
                show_info();
            }
        });
    }
};

var show_info = function(d){
    gen_show_info('readme');
    var el = $(document.getElementById('readme'));

    // https://github.com/fatcloud/PyCV-time/blob/master/experiments/{id}/readme.md
    el.animate({
        'right': 0
    }, {
        duration: 300,
        queue: false,
        complete: function() {
            el.find(".readme-toggle-text").text("\u25b6");
            el.find(".readme-toggle-offset").addClass("open");
        }
    });

    if(typeof d == 'object'){
        var raw_content_base = github_api_raw_path + "master/experiments/" + d.id;
        var readme_uri = github_api_content_path + "experiments/" + d.id + "/readme.md";
        el.children(".readme-body").html("");
        $.ajax({
            url: readme_uri,
            // dataType: 'jsonp',
            // contentType: 'application/vnd.github.v3.raw',
            headers: {
                "Accept": 'application/vnd.github.v3.html; application/json'
            },
            success: function(results) {
                //var content = results.data.content;
                // console.log(results);

                // str.replace(/blue|house|car/gi, function myFunction(x){return x.toUpperCase();});
                var reg = new RegExp("(href|src)=\"(?!http|#)([^\"]+)\"","gi");

                results = results.replace(reg, function(t){
                    var sps = t.split('"');
                    sps[1] = raw_content_base + "/" + sps[1]; 
                    return sps.join('"');
                });

                el.children(".readme-body").html(results);
            },
            error: function(e){
                if(e.responseJSON){
                    // alert(e.responseJSON.message);
                    // var readmeAlert = $(".readme-alert-body");
                    // var readmeAlertMain = readmeAlert.parent();
                    // readmeAlert.html("File 'readme.md' is not found.");
                    // readmeAlertMain.fadeIn('slow').animate({
                    //     'top': 0
                    // }, {
                    //     duration: 'slow',
                    //     queue: false,
                    //     complete: function() {
                    //         // Animation complete.
                    //         setTimeout((function(dom){
                    //             return function(){
                    //                 dom.fadeOut('fast').animate({ top: '-100%' },{
                    //                     duration: 'slow', queue: false
                    //                 });    
                    //             };
                    //         })(readmeAlertMain), 1800);
                    //     }
                    // });
                    show_info(not_found_content);
                }else{
                    alert(e.responseText);
                }
            }
        });
    }else if(typeof d == 'string'){
        el.children(".readme-body").html(d);
    }
    //el.children(".readme-body").html(marked('# Marked in browser\n\nRendered by **'+d.id+'**.'));
};

var hide_info = function(){
    gen_show_info('readme');
    var el = $(document.getElementById('readme'));
    el.animate({
        'right': '-34%'
    }, {
        duration: 300,
        queue: false,
        complete: function() {
            el.find(".readme-toggle-text").text("\u25c0");
            el.find(".readme-toggle-offset").removeClass("open");
        }
    });
    // el.children(".readme-body").html("");
};


var g = svg.append("g").attr("id", "drawing");

g.append("marker")
    .attr("id","triangle")
    .attr("viewBox","0 0 10 10")
    .attr("refX", "10")
    .attr("refY", "5")
    .attr("markerUnits","strokeWidth")
    .attr("markerWidth","20")
    .attr("markerHeight","15")
    .attr("orient","auto")
    .attr("fill", default_link_color)
    .append("path")
    .attr("d", "M 0 0 L 10 5 L 0 10 z");

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
        .attr("marker-end", "url(#triangle)")
        .attr("stroke", default_link_color)

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

    // var sel_count = 0
    // node.on("click", function(d){
    //     node[0][d.index].classList.toggle('selected')

    //     if ($('.selected').length == 1 ){
    //         $('#readme').animate({right: '5vw'});
    //     }
    // });


    var tocolor = "fill";
    var towhite = "stroke";
    if (outline) {
        tocolor = "stroke"
        towhite = "fill"
    }


    function node_size(d) {
        return (d.size)*0.05 || nominal_base_node_size
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
             return node_size(d) * 0.17 + "em"
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

        }).on("click", function(d){
            // To avoid node click after dragEnd event
            if(d3.event.defaultPrevented) return;
            // To do ajax request to get markdown text by specified id.
            show_info(d);
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
        }).on("mousedown", function(){
            if (highlight_node === null){
                //alert("highlight_node is null");
                // hide_info();
            };
        });

    function exit_highlight() {
        highlight_node = null;
        if (focus_node === null) {
            svg.style("cursor", "move");
            if (highlight_color != "white") {
                node.classed('highlighted', false);
                link.classed('highlighted', false);
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

        node.classed('highlighted', function(o){
            return isConnected(d, o)
        });
        // node.attr('class', function(o){
        //     return isConnected(d, o) ? 'node highlighted' : 'node'
        // });

        if (highlight_color != "white") {
            link.classed("highlighted", function(o) {
                return o.source.index == d.index || o.target.index == d.index
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

        for(i = 0, links = force.links(); i < links.length; ++i ){
            s = links[i].source
            t = links[i].target

            dx = t.x - s.x
            dy = t.y - s.y

            ll = Math.sqrt(dx*dx + dy*dy)

            // unit vector from source to target!
            ux = dx / ll
            uy = dy / ll

            // now compute the radius of a node
            rs = node_size(s)
            rt = node_size(t)

            link[0][i].setAttribute("x1", ux*rs + s.x)
            link[0][i].setAttribute("y1", uy*rs + s.y)

            link[0][i].setAttribute("x2", -ux*rt + t.x)
            link[0][i].setAttribute("y2", -uy*rt + t.y)
        }

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

    var init_scale = 0.2 * Math.sqrt( (w * h) / (drawing.getBBox().width * drawing.getBBox().height) );
    var init_x = -(w/2) * (init_scale - 1), init_y = -(h/2) * (init_scale - 1);

    zoom.translate([init_x, init_y]).scale(init_scale).event(g);

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


