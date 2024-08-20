document.addEventListener('DOMContentLoaded', function() {
    const mainVideo = document.getElementById('mainVideo');
    const videoList = document.querySelectorAll('.vid');

    videoList.forEach(videoItem => {
        videoItem.addEventListener('click', function() {
            const videoSource = this.getAttribute('data-src');
            mainVideo.src = videoSource;
            mainVideo.play();
        });
    });
});
