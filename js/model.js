class student{
    name;
    priceHour;
    active;
    lessons;

    constructor(name, priceHour, active){
        this.name = name;
        this.priceHour = priceHour;
        this.active = active;
        this.lessons = [];
    }

    addLesson(lesson){
        this.lessons.push(lesson);
    }

    payLessons(){
        this.lessons.forEach(lesson => {
            lesson.pay();
        })
    }

    order(){
        this.lessons.sort((a, b) => (a.date < b.date) ? 1 : -1);
    }

    delete(){
        this.active = 0;
    }
}

class lesson{
    date;
    time;
    paid;

    constructor(date, time, paid){
        this.date = date;
        this.time = time;
        this.paid = paid;
    }

    pay(){
        this.paid = 1;
    }
}