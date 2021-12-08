#!/usr/bin/haserl
<%
page_title="Camera Preview"
ipaddr=$(printenv | grep HTTP_HOST | cut -d= -f2 | cut -d: -f1)
button() {
  img=$1; alt=$2; id=$(echo "${alt// /-}" | tr '[:upper:]' '[:lower:]')
  echo "<a id=\"${id}\" href=\"\"><img src=\"/img/${img}\" alt=\"${alt}\"></a>"
}
snapshot() {
  echo "<img id=\"snapshot\" src=\"http://${ipaddr}/image.jpg\" class=\"img-fluid\" width=\"1280\" height=\"720\" alt=\"\">"
}
videomp4() {
  echo "<video src=\"http://${ipaddr}/video.mp4\" class=\"img-fluid\" width=\"1280\" height=\"720\"></video>"
}
%>
<%in _header.cgi %>
<h2>Camera Preview</h2>

<div class="row preview">
  <div class="col position-relative mb-4">
    <% snapshot %>
    <div class="control">
      <% button "arrow-up-square-fill.svg" "Pan up" %>
      <% button "dash-square-fill.svg" "Zoom out" %>
      <% button "arrow-left-square-fill.svg" "Pan left" %>
      <% button "camera-fill.svg" "Source" %>
      <% button "arrow-right-square-fill.svg" "Pan right" %>
      <% button "arrow-down-square-fill.svg" "Pan down" %>
      <% button "plus-square-fill.svg" "Zoom in" %>
    </div>
  </div>
</div>

<h3>Available Endpoints</h3>
<p class="small">Detailed information available <a href="https://github.com/OpenIPC/firmware/wiki/majestic_streamer">in the wiki</a>.</p>
<div class="row row-cols-1 row-cols-md-2 g-4">
  <div class="col">
    <div class="card h-100 mb-3">
      <div class="card-header">Web Pages</div>
      <div class="card-body small">
        <dl>
          <dt>http://<%= $ipaddr %>/</dt>
          <dd>HLS live streaming is web browser.</dd>
          <dt>http://<%= $ipaddr %>/mjpeg.html</dt>
          <dd>MJPEG & MP3 live streaming in web browser.</dd>
        </dl>
      </div>
    </div>
  </div>

  <div class="col">
    <div class="card h-100 mb-3">
      <div class="card-header">Video Streams</div>
      <div class="card-body small">
        <dl>
          <dt>http://<%= $ipaddr %>/mjpeg</dt>
          <dd>MJPEG video stream.</dd>
          <dt>http://<%= $ipaddr %>/video.mp4</dt>
          <dd>fMP4 video stream.</dd>
          <dt>rtsp://<%= $ipaddr %></dt>
          <dd>RTSP primary stream ("video0").</dd>
          <dt>rtsp://<%= $ipaddr %>/stream=1</dt>
          <dd>RTSP secondary stream ("video1").</dd>
        </dl>
      </div>
    </div>
  </div>

  <div class="col">
    <div class="card h-100 mb-3">
      <div class="card-header">Still Images</div>
      <div class="card-body small">
        <dl>
          <dt>http://<%= $ipaddr %>/image.jpg</dt>
          <dd>Snapshot in JPEG format.<br>
            Optional parameters:
            <ul class="small">
              <li>width, height - size of resulting image</li>
              <li>qfactor - JPEG quality factor (1-99)</li>
              <li>color2gray - convert to grayscale</li>
              <li>crop - crop resulting image as 16x16x320x320</li>
            </ul>
          </dd>
          <dt>http://<%= $ipaddr %>/image.heif</dt>
          <dd>Snapshot in HEIF format.</dd>
          <dt>http://<%= $ipaddr %>/image.yuv</dt>
          <dd>Snapshot in YUV420 format</dd>
          <dt>http://<%= $ipaddr %>/image.dng</dt>
          <dd>Snapshot in Adobe DNG format (raw)<br>
            (only for v>=2 HiSilicon processors).</dd>
        </dl>
      </div>
    </div>
  </div>

  <div class="col">
    <div class="card h-100 mb-3">
      <div class="card-header">Audio Streams</div>
      <div class="card-body small">
        <dl>
          <dt>http://<%= $ipaddr %>/audio.opus</dt>
          <dd>Opus audio stream.</dd>
          <dt>http://<%= $ipaddr %>/audio.pcm</dt>
          <dd>Raw PCM audio stream.</dd>
          <dt>http://<%= $ipaddr %>/audio.m4a</dt>
          <dd>AAC audio stream.</dd>
          <dt>http://<%= $ipaddr %>/audio.mp3</dt>
          <dd>MP3 audio stream.</dd>
          <dt>http://<%= $ipaddr %>/audio.alaw</dt>
          <dd>A-law compressed audio stream.</dd>
          <dt>http://<%= $ipaddr %>/audio.alaw</dt>
          <dd>A-law compressed audio stream.</dd>
          <dt>http://<%= $ipaddr %>/audio.g711a</dt>
          <dd>G.711 A-law audio stream.</dd>
        </dl>
      </div>
    </div>
  </div>

  <div class="col">
    <div class="card h-100">
      <div class="card-header">Night API</div>
      <div class="card-body small">
        <dl>
          <dt>http://<%= $ipaddr %>/night.on</dt>
          <dd>Turn on night mode.</dd>
          <dt>http://<%= $ipaddr %>/night.off</dt>
          <dd>Turn off night mode.</dd>
          <dt>http://<%= $ipaddr %>/night/invert</dt>
          <dd>Invert current mode.</dd>
        </dl>
      </div>
    </div>
  </div>

  <div class="col">
    <div class="card h-100">
      <div class="card-header">Monitoring</div>
      <div class="card-body small">
        <dl>
          <dt>http://<%= $ipaddr %>/metrics</dt>
          <dd>Standard Node exporter compatible and application-specific metrics for Prometheus.</dd>
        </dl>
      </div>
    </div>
  </div>

</div>

<script>
function updateSnapshot() {
  document.getElementById('snapshot').src = "http://<%= $ipaddr %>/image.jpg?t=" + Date.now();
  setTimeout(updateSnapshot, 3500);
}
window.onload = updateSnapshot;
</script>

<%in _footer.cgi %>
