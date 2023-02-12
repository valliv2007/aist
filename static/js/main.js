document.addEventListener('click', function(event) {
  let e = document.getElementById('cat_nav');
  let menu = document.getElementById('menu_header');
  if (e.contains(event.target)) {
      e.classList.toggle('open');
  } else if (menu.contains(event.target)) {
      document.getElementById('base_wrapper').classList.toggle('open');
  } else {
      e.classList.remove('open');
  }
});


export default class Popup {
    constructor(popupSelector){
      this._popup = document.querySelector(popupSelector);
      //this._handleEscClose = this._handleEscClose.bind(this);
    }
  
    open() {
      this._popup.classList.add('popup_opened');
      document.addEventListener('keydown', this._handleEscClose);
    };
  
    close() {
      this._popup.classList.remove('popup_opened');
      document.removeEventListener('keydown', this._handleEscClose);
    };
  
    _handleEscClose = (evt) => {
      if (evt.key === 'Escape') {
        this.close();
      };
    };
  
    setEventListeners() {
      this._popup.addEventListener('click', (evt) => {
        if (evt.target.classList.contains('popup_opened') ||
        evt.target.classList.contains('popup__close-button')) {
          this.close();
        };
      });
    };
  }

  const r = document.querySelector('.detail-bin-cart__refresh');
  r.addEventListener('click', function(){ alert('work');});

/*
  const refreshBtn = document.getElementById('detail-bin-cart__refresh')

  function sayHello() {
    alert('work');
  }

  refreshBtn.addEventListener('click', sayHello())

  $.ajax({
    url: "url_to_call",
    type: "POST",
    data: {  csrfmiddlewaretoken: "{{ csrf_token }}", //django needs this
             data_item: mydata},
    timeout:0,
    success: function(data){//do something when done
                      //data will be the string returned by HTTPResponse
    }
})*/