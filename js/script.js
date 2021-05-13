let students;
let deletionList;

const container = document.getElementById("container");
const overlay = document.getElementById('overlay');
const history = document.getElementById('history');
const addLesson = document.getElementById('addLesson');
const newStudent = document.getElementById('newStudent');
const messages = document.querySelectorAll('.message');

overlay.addEventListener('click', () =>{
    overlay.classList.remove("active");
    history.classList.remove("active");
    addLesson.classList.remove("active");
    newStudent.classList.remove("active");
})

document.getElementById('cancelHistory').addEventListener('click', () =>{
    overlay.classList.remove("active");
    history.classList.remove("active");
})

document.getElementById('cancelLesson').addEventListener('click', () =>{
    overlay.classList.remove("active");
    addLesson.classList.remove("active");
})

document.getElementById('newStudentBtn').addEventListener('click', () =>{
    document.getElementById('lessonPrice').value = document.getElementById('lessonPrice').defaultValue;
    document.getElementById('studentName').value = "";
    overlay.classList.add('active');
    newStudent.classList.add('active');
})

document.getElementById('cancelStudent').addEventListener('click', () =>{
    overlay.classList.remove("active");
    newStudent.classList.remove("active");
})

document.getElementById('hour').addEventListener('click', () =>{
    document.getElementById('lessonTime').value = 60;
})
document.getElementById('halfAndHour').addEventListener('click', () =>{
    document.getElementById('lessonTime').value = 90;
})
document.getElementById('twoHours').addEventListener('click', () =>{
    document.getElementById('lessonTime').value = 120;
})

document.getElementById('acceptStudent').addEventListener('click', () =>{
    students.push(new student(document.getElementById('studentName').value, document.getElementById('lessonPrice').value));
    saveData();
    loadData();
    overlay.classList.remove('active');
    newStudent.classList.remove('active');
})

let loadData = () => {
    students = [];
    container.innerHTML = "";
    $.ajax(
    {
        url: 'php/loadData.php',
        type: 'POST',
        async: false,

        success: function(result){
            if(result != "null" && result != "false"){
                objects = JSON.parse(result);
                objects.forEach(object => {
                    let stud = new student(object.name, object.priceHour);
                    object.lessons.forEach(less => {
                        stud.addLesson(new lesson(less.date, less.time, less.paid));
                    })
                    students.push(stud);
                });
                
                students.forEach(student => {
                    container.appendChild(createRow(student));
                });
            }else{
                console.log("Has been an error on load data");
            }
        },
         error: function (xhr, ajaxOptions, thrownError) {
            console.log("Error: ", xhr.status, 0);
        }
    });
}

let saveData = () => {
    students.forEach(student => {
        student.order();
    })

    $.ajax(
        {
            url: 'php/saveData.php',
            data: {"data": JSON.stringify(students)},
            type: 'POST',
            async: false,
    
            success: function(result){
                console.log(result);
            },
             error: function (xhr, ajaxOptions, thrownError) {
                console.log("Error: ", xhr.status, 0);
            }
        });
}

let createRow = (student) => {
    let classTime = student.lessons.reduce(reducer, 0);
    let price = classTime * (student.priceHour / 60) + " €";

    var img1 = document.createElement("img");
    img1.src = "images/scroll.png";
    var img2 = document.createElement("img");
    img2.src = "images/add.png";

    var newLesson = document.createElement("div");
    newLesson.classList.add("newLesson");
    newLesson.appendChild(img2);
    newLesson.addEventListener("click", () =>{
        document.getElementById('lessonTime').value = document.getElementById('lessonTime').defaultValue;
        document.getElementById('lessonDate').valueAsDate = new Date();
        overlay.classList.add('active');
        addLesson.classList.add('active');
        document.getElementById('acceptLesson').addEventListener('click', () =>{
            student.addLesson(new lesson(document.getElementById('lessonDate').value, parseInt(document.getElementById('lessonTime').value), 0));
            saveData();
            overlay.classList.remove('active');
            addLesson.classList.remove('active');
            loadData();
        }, { once: true })
    })

    var time = document.createElement("p");
    time.classList.add("m-auto");
    var timeText = document.createTextNode(secToTime(classTime));
    time.appendChild(timeText);
    var payment = document.createElement("p");
    payment.classList.add("m-auto");
    var paymentText = document.createTextNode(price);
    payment.appendChild(paymentText);

    var subdata1 = document.createElement("div");
    subdata1.classList.add("subdata");
    subdata1.appendChild(time);
    var subdata2 = document.createElement("div");
    subdata2.classList.add("subdata");
    subdata2.appendChild(payment);

    var data2 = document.createElement("div");
    data2.classList.add("data2");
    data2.appendChild(subdata1);
    data2.appendChild(subdata2);
    data2.addEventListener("click", () =>{
        overlay.classList.add('active');
        removeElements( document.querySelectorAll(".historyData") );
        deletionList = [];
        student.lessons.forEach(lesson =>{
            history.appendChild(createHistory(lesson));
        })
        document.getElementById('pay').addEventListener('click', () =>{
            student.payLessons();
            saveData();
            loadData();
            overlay.classList.remove("active");
            history.classList.remove("active");
        })
        document.getElementById('delete').addEventListener('click', () =>{
            deleteLessons(student);

            removeElements( document.querySelectorAll(".historyData") );
            deletionList = [];
            student.lessons.forEach(lesson =>{
                history.appendChild(createHistory(lesson));
            })

            loadData();
        })
        history.classList.add('active');
    });

    var name = document.createElement("p");
    name.classList.add("m-auto");
    var nameText = document.createTextNode(student.name);
    name.appendChild(nameText);

    var data1 = document.createElement("div");
    data1.classList.add("data1");
    data1.appendChild(name);

    var data = document.createElement("div");
    data.classList.add("data");
    data.appendChild(data1);
    data.appendChild(data2);
    data.appendChild(newLesson);
    
    return data;
}

const createHistory = (lesson) => {
    var date = document.createElement("p");
    var dateText = document.createTextNode(lesson.date);
    date.appendChild(dateText);
    var time = document.createElement("p");
    var timeText = document.createTextNode(secToTime(lesson.time));
    lesson.paid ? time.classList.add('green') : time.classList.add('red');
    time.appendChild(timeText);

    var dateCont = document.createElement("div");
    dateCont.classList.add("date");
    dateCont.appendChild(date);
    var timeCont = document.createElement("div");
    timeCont.classList.add("time");
    timeCont.appendChild(time);

    var historyData = document.createElement("div");
    historyData.classList.add("historyData");
    historyData.appendChild(dateCont);
    historyData.appendChild(timeCont);
    
    let t0;
    let setint  = '';
    historyData.addEventListener('mousedown', () => {
        clearInterval(setint);
        t0 = performance.now();
        setint = setInterval(function () {
            console.log(deletionList);
            if(performance.now() - t0 > 300){
                var index = deletionList.indexOf(lesson);
                if (index > -1) {
                    deletionList.splice(index, 1);
                }else{
                    deletionList.push(lesson);
                }
                historyData.classList.toggle("selected");
                clearInterval(setint);
            }
        },50);
    });

    historyData.addEventListener('mouseup', () => { 
        clearInterval(setint);
    });

    return historyData;
}

const deleteLessons = (student) => {
    if(deletionList.length > 0){
        let errors = 0;
        deletionList.forEach(deletion => {
            var index = student.lessons.indexOf(deletion);
            if (index > -1) {
                student.lessons.splice(index, 1);
            }else{
                errors++;
            }
        })
        if(errors > 0){
            document.getElementById('message').innerHTML = 'No se han borrado todos los elementos';
            message.classList.add('messageWrong');
        }else{
            document.getElementById('message').innerHTML = 'Elementos borrados';
            message.classList.add('messageSucssess');
            saveData();
        }
    }else{
        document.getElementById('message').innerHTML = 'No has seleccionado nada';
        message.classList.add('messageWrong');
    }

    messages.forEach(message => {
        message.classList.add('faceinout');
    })
}

const reducer = (accumulator, currentValue) => {
    if(currentValue.paid == 0){
        return accumulator + currentValue.time;
    }
    return accumulator;
};

const removeElements = (elms) => elms.forEach(el => el.remove());

const secToTime = (min) =>{
    var hr  = Math.floor(min / 60);
    var min = Math.floor(min - hr * 60);

    if(hr < 10){
        hr = "0" + hr;
    }
    if(min < 10){
        min = "0" + min;
    }

    return(hr + "h " + min + "m");
}

messages.forEach(message => {
    message.addEventListener('animationend', () => {
        message.classList.remove('faceinout');
        message.classList.remove('messageSucssess');
        message.classList.remove('messageWrong');
    })
})

loadData();

// students.forEach(student => {
//     student.order();
// })
// console.log(students);