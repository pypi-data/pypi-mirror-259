def command():
    """
    Mark the current location in job logs with special tag.

    This command can be used before `gitoptim analyse logs --after-last-tag` command.
    It instructs the SDK to analyse only the logs that appear after the tag that is places by this command.

    Example:
    $ npm install
    $ gitoptim tag
    $ npm run test
    $ gitoptim analyse logs --after-last-tag

    Above example will only analyse from `npm run test` but not from `npm install`.
    """
