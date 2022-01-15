var HighwayModule = function(canvas_width, canvas_height) {
    let canvas_tag = "<canvas width='" + canvas_width + "' height='" + canvas_height + "' ";
    canvas_tag += "style='border:1px dotted'></canvas>";
    let canvas = $(canvas_tag)[0];
    $("#elements").append(canvas);
    let context = canvas.getContext("2d");

    this.render = function(data) {
        console.log(data)
        createLanes();

        for(let i=0; i<data.length; i++) {
            if(data[i].type === "Truck") {
                createTruckAgent(i);
            }
            if(data[i].type === "FamilyCar") {
                createFamilyCarAgent(i);
            }
            if(data[i].type === "SportsCar") {
                createSportsCarAgent(i);
            }
            if(data[i].type === "Construction") {
                createConstructionAgent(i);
            }
        }
    };

    this.reset = function() {
        context.strokeStyle = 'black';
        context.clearRect(0, 0, canvas.width, canvas.height);
    };

    function createLanes() {
        context.strokeStyle = 'black';
        context.clearRect(0, 0, canvas.width, canvas.height);
        context.rect(0, 0, 3000, 30);
        context.rect(0, 30, 3000, 30);
        context.setLineDash([5, 10]);
        context.stroke();
    }

    function createTruckAgent(i) {
        context.fillStyle = 'green';
        context.fillRect(i*50, 5, 45, 20);
    }

    function createFamilyCarAgent(i) {
        context.fillStyle = 'blue';
        context.fillRect(i*50, 5, 35, 20);
    }

    function createSportsCarAgent(i) {
        context.fillStyle = 'red';
        context.fillRect(i*50, 5, 30, 20);
    }

    function createConstructionAgent(i) {
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
    }
};