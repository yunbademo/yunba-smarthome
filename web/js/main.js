/**
 * [config description]
 * @type {Object}
 */
var config = {
    APPKEY: '563c4afef085fc471efdf803',
    TOPIC: 'smart_home_topic',
    ALIAS: 'pi_house',
}
var yunba = new Yunba({
    server: 'sock.yunba.io',
    port: 3000,
    appkey: config.APPKEY
});

$(document).ready(function() {
    //初始化云巴服务器
    init();
    //初始化播放器
    var rp = new audioPlayer();
    rp.init();
    //初始化情景模式
    var sm = new sceneMode();
    sm.init();

    window.status_ll = false;
    $(".llinput").on('click', function(e) {
        if (!status_ll) {
            $("input[id='lloff']").prop("checked", "true");
        } else {
            $("input[id='llon']").prop("checked", "true");
        }
        status_ll = !status_ll;
        var arr = checkedpara();
        if ($("input[name='ll']:checked").attr("id") == "llon") {
            publish_to_alias(config.ALIAS, '{"act":"light_off", "name":"living"}');
        } else {
            publish_to_alias(config.ALIAS, '{"act":"light_on", "name":"living", "freq":' + arr[0] + ', "dc":' + arr[1] + '}');
        }
    });


    window.status_bl = false;
    $(".blinput").on('click', function(e) {
        if (!status_bl) {
            $("input[id='bloff']").prop("checked", "true");
        } else {
            $("input[id='blon']").prop("checked", "true");
        }
        status_bl = !status_bl;
        var arr = checkedpara();
        if ($("input[name='bl']:checked").attr("id") == "blon") {
            publish_to_alias(config.ALIAS, '{"act":"light_off", "name":"bedroom"}');
        } else {
            publish_to_alias(config.ALIAS, '{"act":"light_on", "name":"bedroom","freq":' + arr[0] + ', "dc":' + arr[1] + '}');

        }

    });

    window.status_pl = false
    $(".plinput").on('click', function(e) {
        if (!status_pl) {
            $("input[id='ploff']").prop("checked", "true");
        } else {
            $("input[id='plon']").prop("checked", "true");
        }
        status_pl = !status_pl;
        var arr = checkedpara();
        if ($("input[name='pl']:checked").attr("id") == "plon") {
            publish_to_alias(config.ALIAS, '{"act":"light_off", "name":"porch"}');
        } else {

            publish_to_alias(config.ALIAS, '{"act":"light_on", "name":"porch","freq":' + arr[0] + ', "dc":' + arr[1] + '}');
        }

    });

    window.status_door = false
    $(".doorinput").on('click', function(e) {
        if (!status_door) {
            $("input[id='close']").prop("checked", "true");
        } else {
            $("input[id='open']").prop("checked", "true");
        }
        status_door = !status_door;
        if ($("input[name='door']:checked").attr("id") == "open") {
            publish_to_alias(config.ALIAS, '{"act":"door_close"}');
        } else {
            publish_to_alias(config.ALIAS, '{"act":"door_open"}');
        }
    });
});

function getMessage() {
    yunba.set_message_cb(function(data) {
        var h = 0;
        var t = 0;
        console.log(data);
        var msg = JSON.parse(data.msg);
        if (msg.act == "humtem") {
            h = msg.h + "%";
            t = msg.t + "℃";

            var t_height = 0;
            if (msg.t < 0) {
                //73保证不溢出
                t_height = (((20 + Number(msg.t)) / 73) * 100).toFixed(1) + "%";
                console.log(t_height);
            } else if (msg.t == 0) {
                t_height = "28.5%";
            } else {

                t_height = (((Number(msg.t) + 20) / 73) * 100).toFixed(1) + "%";
                console.log((Number(msg.t) + 20) / 73);
            }
            //温度计范围－20～50摄氏度
            console.log(msg.t);
            $(".amount").css("height", t_height);
            $(".total").html(t);
            $(".total").css("bottom", t_height);
            //湿度计
            $(".amount_b").css("height", h);
            $(".total_b").html(h);
            $(".total_b").css("bottom", h);
        } else if (msg.act == "door") {
            if (msg.st == "closed") {
                window.status_door = false;
                $("input[id='open']").prop("checked", "true");
            } else {
                window.status_door = true;
                $("input[id='close']").prop("checked", "true");
            }
        } else if (msg.act == "light") {
            if (msg.living == "on") {
                $(".tower").addClass("bright");
                window.status_ll = true;
                $("input[id='lloff']").prop("checked", "true");
            } else {
                $(".tower").removeClass("bright");
                window.status_ll = false;
                $("input[id='llon']").prop("checked", "true");
            }

            if (msg.bedroom == "on") {
                $(".house ul li:lt(3)").css("background", "#E4FD14");
                window.status_bl = true;
                $("input[id='bloff']").prop("checked", "true");
            } else {
                $(".house ul li:lt(3)").css("background", "#6D6D6D");
                window.status_bl = false;
                $("input[id='blon']").prop("checked", "true");
            }

            if (msg.porch == "on") {
                $(".house ul li:gt(2)").css("background", "#E4FD14")
                window.status_pl = true;
                $("input[id='ploff']").prop("checked", "true");
            } else {
                $(".house ul li:gt(2)").css("background", "#6D6D6D");
                window.status_pl = false;
                $("input[id='plon']").prop("checked", "true");
            }
        } else if (msg.act == "media") {
            if (msg.st == "stop") {
                $("#stop").addClass("hide");
                $("#play").removeClass("hide");
                $("#musicUrl").removeAttr("readonly")
            } else if (msg.st == "play") {
                $("#play").addClass("hide");
                $("#stop").removeClass("hide");
                $("#musicUrl").attr("disabled");
                $("#musicUrl").attr("readonly", "true");
            } else if (msg.st == "resume") {
                $("#resume").addClass("hide");
                $("#pause").removeClass("hide");
            } else if (msg.st == "pause") {
                $("#pause").addClass("hide");
                $("#resume").removeClass("hide");
            }
        }
    });

}

/**
 * 随机ID生成
 * 
 */
function MathRand() {
    var myDate = new Date();
    var mytime = myDate.getTime();
    var Num = "";
    for (var i = 0; i < 6; i++) {
        Num += Math.floor(Math.random() * 10);
    }
    Num = Num + "-" + mytime;
    return Num;
};

/**
 * @return {[type]}
 */
function init() {
    var randomID = MathRand();
    yunba.init(function(success) {
        if (success) {

            yunba.connect_by_customid('' + randomID + '', function(success, msg, sessionid) {
                if (success) {
                    console.log('你已成功连接到消息服务器，会话ID：' + sessionid);
                    $(".wrapper").remove();
                    $("body").css("background", "url(../wood-tile-background.jpg");
                    $(".container-fluid").removeClass("hide");
                    getMessage();
                    subscribe(config.TOPIC);
                } else {
                    console.log(msg);
                }
            });
        }
    });
}
/**
 * @param  {[type]}
 * @return {[type]}
 */
function subscribe(topic) {
    yunba.subscribe({
            'topic': topic
        },
        function(success, msg) {
            if (success) {
                console.log('你已成功订阅频道：' + topic + '');
                publish_to_alias(config.ALIAS, '{"act":"report_req"}');
            } else {
                console.log(msg);
            }
        }
    );
}

/**
 * @param  {[type]}
 * @param  {[type]}
 * @param  {[type]}
 * @return {[type]}
 */
function publish_to_alias(alias, msg) {
    console.log(msg);
    yunba.publish_to_alias({
        'alias': alias,
        'msg': msg,
    }, function(success, msg) {
        if (!success) {
            console.log(msg);
        }
    });
}

// 设置模态框
/**
 * @param  {[type]}
 * @param  {[type]}
 * @return {[type]}
 */
function infoSettings(info, modal) {
    $('#' + modal + ' .modal-body p').text(info);

}
/**
 * @return {[type]}
 */
function checkedpara() {
    var fre = ((($(".ui-slider-range:first").css("width").split("px")[0]) / 248) * 100).toFixed(0);
    var dc = ((($(".ui-slider-range:last").css("width").split("px")[0]) / 248) * 100).toFixed(0);
    var arr = [];
    $(".sliderfre > span:last ").html(fre);
    $(".sliderdc > span:last").html(dc);
    arr[0] = fre;
    arr[1] = dc;
    return arr;
}

function audioPlayer() {
    this.init = function() {
        this.stop();
        this.play();
        this.resume();
        this.pause();
        this.up();
        this.down();
    };
    this.play = function() {
        console.log("play");
        $("#play").on('click', function(e) {

            var url = $("#musicUrl").val();
            if (url == '') {
                infoSettings("The music URL is empty！", "myModal");
                $('#myModal').modal('show');

                return false;
            };
            url = "/home/pi/media/" + url;

            publish_to_alias(config.ALIAS, '{"act":"media_play", "path":"' + url + '"}');
            $("#play").addClass("hide");
            $("#stop").removeClass("hide");
            $("#musicUrl").attr("disabled");
            $("#musicUrl").attr("readonly", "true");
        })
    };
    this.stop = function() {
        console.log("stop");
        $("#stop").on('click', function(e) {

            publish_to_alias(config.ALIAS, '{"act":"media_stop"}');
            $("#stop").addClass("hide");
            $("#play").removeClass("hide");
            $("#musicUrl").removeAttr("readonly")
        })
    };
    this.resume = function() {
        console.log("resume");
        $("#resume").on('click', function(e) {
            $("#resume").addClass("hide");
            $("#pause").removeClass("hide");
            publish_to_alias(config.ALIAS, '{"act":"media_resume"}');

        })
    };
    this.pause = function() {
        console.log("pause");
        $("#pause").on('click', function(e) {
            $("#pause").addClass("hide");
            $("#resume").removeClass("hide");
            publish_to_alias(config.ALIAS, '{"act":"media_pause"}');

        })
    };
    this.up = function() {
        console.log("up");
        $("#up").on('click', function(e) {

            publish_to_alias(config.ALIAS, '{"act":"media_inc_vol"} ');

        })
    };
    this.down = function() {
        console.log("down");
        $("#down").on('click', function(e) {

            publish_to_alias(config.ALIAS, '{"act":"media_dec_vol"}');

        })
    };
}

function sceneMode() {
    this.init = function() {
        var that = this;
        $("#normal").on('click', function(e) {
            that.normal();
        });
        $("#outgoing").on('click', function(e) {
            that.outgoing();
        });
        $("#sleep").on('click', function(e) {
            that.sleep();
        });
        $("#party").on('click', function(e) {
            that.party();
        })

    }
    this.normal = function() {
        publish_to_alias(config.ALIAS, '{"act":"light_on", "name":"living", "freq":60, "dc":100}');
        publish_to_alias(config.ALIAS, '{"act":"light_on", "name":"bedroom", "freq":60, "dc":100}');
        publish_to_alias(config.ALIAS, '{"act":"light_on", "name":"porch", "freq":60, "dc":100}');
        publish_to_alias(config.ALIAS, '{"act":"media_stop"}');
        publish_to_alias(config.ALIAS, '{"act":"door_close"}');

    };
    this.outgoing = function() {
        publish_to_alias(config.ALIAS, '{"act":"light_off", "name":"living"}');
        publish_to_alias(config.ALIAS, '{"act":"light_off", "name":"bedroom"}');
        publish_to_alias(config.ALIAS, '{"act":"light_off", "name":"porch"}');

        publish_to_alias(config.ALIAS, '{"act":"media_stop"}');
        publish_to_alias(config.ALIAS, '{"act":"door_close"}');

    };
    this.sleep = function() {
        publish_to_alias(config.ALIAS, '{"act":"light_on", "name":"living", "freq":60, "dc":10}');
        publish_to_alias(config.ALIAS, '{"act":"light_off", "name":"bedroom"}');
        publish_to_alias(config.ALIAS, '{"act":"light_on", "name":"porch", "freq":60, "dc":100}');

        publish_to_alias(config.ALIAS, '{"act":"media_stop"}');
        publish_to_alias(config.ALIAS, '{"act":"door_close"}');
    };
    this.party = function() {
        publish_to_alias(config.ALIAS, '{"act":"light_on", "name":"living", "freq":10, "dc":80}');
        publish_to_alias(config.ALIAS, '{"act":"light_on", "name":"bedroom", "freq":10, "dc":60}');
        publish_to_alias(config.ALIAS, '{"act":"light_on", "name":"porch", "freq":10, "dc":100}');
        publish_to_alias(config.ALIAS, '{"act":"media_inc_vol" }');
        publish_to_alias(config.ALIAS, '{"act":"media_play","path":"/home/pi/media/Stickwitu.mp3"}');
        publish_to_alias(config.ALIAS, '{"act":"door_open"}');
    };
}
