import unreal

def save_render_target_to_disk(render_target, file_path):
    # Get the Asset Tools module
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    
    # Create a new texture asset from the render target
    texture = asset_tools.create_unique_asset_name('/Game/SavedTextures/', 'CapturedTexture')[0]
    texture2d = unreal.EditorAssetLibrary.create_asset(texture, None, unreal.Texture2D, unreal.TextureFactory())
    
    # Export the texture to a disk location
    success = unreal.EditorAssetLibrary.export_render_target(render_target, file_path)
    
    if success:
        unreal.log(f"Saved render target to {file_path}")
    else:
        unreal.log("Failed to save render target")

# Example usage:
# save_render_target_to_disk('/Game/PanoramaRenderTarget', 'C:/YourFolder/CapturedImage.png')
