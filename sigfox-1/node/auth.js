var basicAuth = require('basic-auth');

exports.basicAuthentication = function(req, res, next) {

    function unauthorized(response) {
        res.set('WWW-Authenticate', 'Basic realm=Authorization Required');
        return res.sendStatus(401);

    };

    var user = basicAuth(req);

    if (!user || !user.name || !user.pass) {
        return unauthorized(res);
    };

    if (user.name === 'testUser' && user.pass === 'testPass') {
        return next();
    } else {
        Console.error("Authorized : " + user.name + ":" + user.pass);
        return unauthorized(res);
    };

};