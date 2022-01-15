var HighwayModule = function(canvas_width, canvas_height) {
    let canvas_tag = "<canvas width='" + canvas_width + "' height='" + canvas_height + "' ";
    canvas_tag += "style='border:1px dotted'></canvas>";
    let canvas = $(canvas_tag)[0];
    $("#elements").append(canvas);
    let context = canvas.getContext("2d");

    this.render = function(data) {
        createLanes();

        for(let i=0; i<data.length; i++) {
            if(data[i].type === "Truck") {
                createTruckAgent(data[i].x, data[i].y);
            }
            if(data[i].type === "FamilyCar") {
                createFamilyCarAgent(data[i].x, data[i].y);
            }
            if(data[i].type === "SportsCar") {
                createSportsCarAgent(data[i].x, data[i].y);
            }
            if(data[i].type === "Construction") {
                createConstructionAgent(data[i].x, data[i].y);
            }
            if(data[i].type === "Exit") {
                createExitAgent(data[i].x, data[i].y);
            }
            if(data[i].type === "Entrance") {
                createEntranceAgent(data[i].x, data[i].y);
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

    function createTruckAgent(x, y) {
        context.fillStyle = 'yellow';
        if (y === 0)
            context.fillRect(x*50, 5, 45, 20);
        else
            context.fillRect(x*50, 35, 45, 20);
    }

    function createFamilyCarAgent(x, y) {
        context.fillStyle = 'blue';
        if (y === 0)
            context.fillRect(x*50, 5, 35, 20);
        else
            context.fillRect(x*50, 35, 35, 20);
    }

    function createSportsCarAgent(x, y) {
        context.fillStyle = 'purple';
        if (y === 0)
            context.fillRect(x*50, 5, 30, 20);
        else
            context.fillRect(x*50, 35, 30, 20);
    }

    function createConstructionAgent(x, y) {
         context.beginPath();
         if(y === 1) {
             y = 32
             y_bottom = 58
         } else {
             y = 2
             y_bottom = 28
         }
         context.moveTo(x*50, y);
         context.lineTo(x*50+48, y_bottom);
         context.moveTo(x*50, y_bottom);
         context.lineTo(x*50+48, y);
         context.strokeStyle = 'red';
         context.setLineDash([]);
         context.stroke();
         context.fillStyle = 'black';
         context.fillRect(x*50, y, 48, 26);
         context.stroke();
    }

     function createExitAgent(x, y) {
         context.beginPath();
         if(y === 1) {
             y = 32
             y_bottom = 58
         } else {
             y = 2
             y_bottom = 28
         }
         context.fillStyle = 'red';
         context.fillRect(x*50, y, 48, 26);
         context.stroke();
    }

     function createEntranceAgent(x, y) {
         context.beginPath();
         if(y === 1) {
             y = 32
             y_bottom = 58
         } else {
             y = 2
             y_bottom = 28
         }
         context.fillStyle = 'green';
         context.fillRect(x*50, y, 48, 26);
         context.stroke();
    }
};