var dataEvent = require('./events');

var  messageHandler = function(m) {
            console.log(m);
        }

dataEvent.subscribe('sigfox_data', messageHandler)