class TweetPhotoStatus:
    PENDING = 0
    APPROVED = 1
    REJECTED = 2

# 在admin中会使用该多元组以渲染
TWEET_PHOTO_STATUS_CHOICES = (
    (TweetPhotoStatus.PENDING, 'Pending'),
    (TweetPhotoStatus.APPROVED, 'Approved'),
    (TweetPhotoStatus.REJECTED, 'Rejected'),
)
