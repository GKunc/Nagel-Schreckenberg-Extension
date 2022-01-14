var HighwayModule = function(bins, canvas_width, canvas_height) {
    var canvas_tag = "<canvas width='" + canvas_width + "' height='" + canvas_height + "' ";
    canvas_tag += "style='border:1px dotted'></canvas>";
    var canvas = $(canvas_tag)[0];
    $("#elements").append(canvas);
    var context = canvas.getContext("2d");

    // Create the chart object
    this.render = function(data) {
        console.log(data)
        context.rect(0, 0, 1000, 50);
        context.rect(0, 50, 1000, 50);
        context.setLineDash([5, 10]);
        context.stroke();

        for(var i=0; i<data.length; i++) {
            if(data[i].type === "Truck") {
                context.fillStyle = 'green';
                context.fillRect(i*50, 5, 40, 40);
            }
            if(data[i].type === "FamilyCar") {
                context.fillStyle = 'blue';
                context.fillRect(i*50, 5, 40, 40);
            }
            if(data[i].type === "SportsCar") {
                context.fillStyle = 'red';
                context.fillRect(i*50, 5, 40, 40);
            }
            if(data[i].type === "Construction") {
                context.fillStyle = 'black';
                context.fillRect(i*50, 5, 40, 40);
            }
        }
    };

    this.reset = function() {
        context.rect(0, 0, 1000, 50);
        context.rect(0, 50, 1000, 50);
        context.setLineDash([5, 10]);
        context.stroke();
    };
};