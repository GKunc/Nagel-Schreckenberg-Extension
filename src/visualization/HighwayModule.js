var HighwayModule = function(canvas_width, canvas_height) {
    var canvas_tag = "<canvas width='" + canvas_width + "' height='" + canvas_height + "' ";
    canvas_tag += "style='border:1px dotted'></canvas>";
    var canvas = $(canvas_tag)[0];
    $("#elements").append(canvas);
    var context = canvas.getContext("2d");

    // Create the chart object
    this.render = function(data) {
        console.log(data)
        context.strokeStyle = 'black';
        context.clearRect(0, 0, canvas.width, canvas.height);
        context.rect(0, 0, 3000, 30);
        context.rect(0, 30, 3000, 30);
        context.setLineDash([5, 10]);
        context.stroke();

        for(var i=0; i<data.length; i++) {
            if(data[i].type === "Truck") {
                context.fillStyle = 'green';
                context.fillRect(i*50, 5, 45, 20);
            }
            if(data[i].type === "FamilyCar") {
                context.fillStyle = 'blue';
                context.fillRect(i*50, 5, 35, 20);
            }
            if(data[i].type === "SportsCar") {
                context.fillStyle = 'red';
                context.fillRect(i*50, 5, 30, 20);
            }
            if(data[i].type === "Construction") {
                context.beginPath();
                context.moveTo(i*50, 2);
                context.lineTo(i*50+48, 28);
                context.moveTo(i*50, 28);
                context.lineTo(i*50+48, 2);
                context.strokeStyle = 'red';
                context.setLineDash([]);
                context.stroke();
                context.fillStyle = 'black';
                context.fillRect(i*50, 2, 48, 26);
                context.stroke();

                // context.fillText("blah", i*60, 15);
            }
        }
    };

    this.reset = function() {
        context.strokeStyle = 'black';
        context.clearRect(0, 0, canvas.width, canvas.height);
    };
};