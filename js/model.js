class student{
    name;
    priceHour;
    lessons;

    constructor(name, priceHour){
        this.name = name;
        this.priceHour = priceHour;
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