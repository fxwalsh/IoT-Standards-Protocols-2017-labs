var express = require('express');
var router = express.Router();
var auth = require("../auth.js");
var MongoClient = require('mongodb').MongoClient;
var dataEvent = require("../events.js");
var assert = require('assert');


// Connection URL
var url = process.env.dbURL;

/* GET home page. */
router.get('/', function(req, res, next) {
    res.render('index', {
        title: 'Express'
    });
});

/* POST data */
router.post('/data', auth.basicAuthentication, function(req, res, next) {
    req.checkBody("temp", "Did not recieve valid data").notEmpty().isInt();
    req.checkBody("light", "Did not recieve valid data").notEmpty().isInt();
    var errors = req.validationErrors();
    if (errors) {
        res.send(errors);
        return;
    } else {
        // Normal processing
        dataEvent.publish('sigfox_data', req.body);
        // Use connect method to connect to the Mongo db Server
        MongoClient.connect(url, function(err, db) {
            assert.equal(err, null);
            var collection = db.collection('sensor_data');
            collection.insertOne(
                req.body,
                function(err, result) {
                    assert.equal(err, null);
                    res.send("Post Successful");
                    db.close();
                });

        });
    }


});

module.exports = router;
